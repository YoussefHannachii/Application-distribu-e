import sys
import mysql.connector
from datetime import datetime
import Ice
import subprocess
import requests
import psutil

# Importer le module généré à partir du fichier Slice
import StreamingAndroid

def generate_query_from_string(input_string):
    # Diviser la phrase en mots
    words = input_string.split()

    # Initialiser la partie de la requête SQL
    sql_query = "SELECT * FROM song WHERE"

    # Ajouter une condition pour chaque mot
    for word in words:
        # Ajouter le mot à la requête SQL avec le format approprié
        sql_query += f" title LIKE CONCAT('%{word}%') Or"

    # Retirer le dernier "Or" et ajouter le point-virgule
    sql_query = sql_query[:-3] + ";"

    return sql_query



class MonInterfaceI(StreamingAndroid.InterfaceStreamingAndroid):

    def streamAudioWithTitle(self, titreExtraitAvecNlp,current=None):
        print(titreExtraitAvecNlp)
        try:
            # Arrête le processus VLC s'il est déjà en cours d'exécution
            for process in psutil.process_iter():
                if "vlc" in process.name():
                    process.kill()
            
            # Établir la connexion à la base de données
            conn = mysql.connector.connect(
                user='root',
                password='root',
                host='localhost',
                database='mini_spotify',
                raise_on_warnings=True
            )

            cursor = conn.cursor(dictionary=True)
            #Generation de la requete sql avec une clause pour chaque mot present sur la phrase extrait pour une plus grande precision
            sqlQuery=generate_query_from_string(titreExtraitAvecNlp)
            cursor.execute(sqlQuery)

            # Récupérer les résultats
            resultats = cursor.fetchall()
            print(resultats)

            if len(resultats) == 0:
                raise StreamingAndroid.SongNotFoundException("La chanson n'a pas été trouvée.")
            elif len(resultats) == 1:
                command = [
                "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
                "--intf", "dummy",
                resultats[0]['emplacement'],
                "--sout", f"#transcode{{acodec=mp3,ab=128,channels=2,samplerate=44100}}:http{{mux=mp3,dst=:8082/stream}}"
                ]
                subprocess.Popen(command)
                return "http://localhost:8082/stream"
            else:
                titres = []
                for resultat in resultats:
                    titres.append(resultat['title'])
                data = {
                    'titreExtraitParNlp': titreExtraitAvecNlp,
                    'titreTrouvesDansBd': titres
                }
                response = requests.post('http://127.0.0.1:5000/compare', json=data)

                # Vérifier si la requête a réussi (code de statut 200)
                if response.status_code == 200:
                    # Récupérer la réponse de l'API sous forme de dictionnaire JSON
                    resultApi = response.json()
                    
                    # Vérifier si la clé 'phrase_similaire' est présente dans le résultat
                    if 'titrePlusPrecis' in resultApi:
                        # Ajouter la phrase similaire à la variable phrases
                        titrePlusPrecis = resultApi['titrePlusPrecis']
                        for resultat in resultats:
                            if resultat['title']==titrePlusPrecis:
                                musiqueStream = resultat
                        print(musiqueStream)
                        command = [
                        "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
                        "--intf", "dummy",
                        musiqueStream['emplacement'],
                        "--sout", f"#transcode{{acodec=mp3,ab=128,channels=2,samplerate=44100}}:http{{mux=mp3,dst=:8082/stream}}"
                        ]
                        subprocess.Popen(command)
                        return "http://localhost:8082/stream"
                    else:
                        print("La clé 'phrase_similaire' est absente dans le résultat.")
        except mysql.connector.Error as err:
            print(f"Erreur MySQL: {err}")
            raise Ice.UnknownException("Erreur lors de la récupération de la chanson.")

        finally:
            # Fermer la connexion à la base de données
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

# Configuration d'Ice et initialisation du serveur
with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("InterfaceStreamingAndroidAdapter", "default -p 10008")
    object = MonInterfaceI()
    adapter.add(object, communicator.stringToIdentity("InterfaceStreamingAndroid"))
    adapter.activate()
    print("Server working and waiting for requests!")
    print("Server listening on endpoints:", adapter.getEndpoints())
    communicator.waitForShutdown()
