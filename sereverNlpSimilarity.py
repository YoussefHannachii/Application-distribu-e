from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Charger le modèle français de spaCy
nlp = spacy.load("fr_core_news_sm")

# Liste des formes verbales autorisées
verbes_autorises = {'jouer', 'arrêter', 'stop', 'pause' , 'arrête' , 'joue' ,'pauser','relancer'}

def extraire_verbe_et_sujet(phrase):
    # Analyser la phrase avec spaCy
    doc = nlp(phrase)

    # Initialiser le verbe et le sujet à None
    verbe = None
    sujet = None

    # Parcourir les tokens de la phrase
    for token in doc:
        # Vérifier si le token est un verbe et s'il est dans la liste des verbes souhaités
        if token.pos_ == 'VERB'  and token.lemma_ in verbes_autorises or token.text == 'stoppe' or token.text == 'relance' :
            
            verbe = token.text

            #Essai avec la suppression des mots vides de la phrase mais cela peut causer des problemes de precision de recherche apres

            #sujet_tokens = [tok.text for tok in doc[token.i + 1:] if tok.text.lower() not in mots_vides]
            #sujet = ' '.join(sujet_tokens)
            
            # Prendre tout ce qui vient après le verbe jusqu'à la fin de la phrase
            sujet = ' '.join([tok.text for tok in doc[token.i + 1:]])
            break
    print(verbe)
    return {'verbe': verbe, 'sujet': sujet}

@app.route('/compare', methods=['POST'])
def compare_sentences():
    # Récupérer les données JSON de la requête
    data = request.json
    titreExtraitParNlp = data['titreExtraitParNlp']
    titreTrouvesDansBd = data['titreTrouvesDansBd']

    # Initialisation de la similarité maximale et de la phrase la plus similaire
    max_sim = 0
    titrePlusPrecis = ""

    # Calculer la similarité cosinus entre la phrase de référence et chaque phrase à comparer
    for phrase in titreTrouvesDansBd:
        sim = nlp(titreExtraitParNlp).similarity(nlp(phrase))
        if sim > max_sim:
            max_sim = sim
            titrePlusPrecis = phrase

    print(titrePlusPrecis)
    # Retourner la phrase la plus similaire au format JSON
    return jsonify({'titrePlusPrecis': titrePlusPrecis})

@app.route('/extract', methods=['POST'])
def extract_verb_subject():
    # Récupérer les données JSON de la requête
    data = request.json
    phrase = data['phrase']

    # Extraire le verbe et le sujet de la phrase et retourner les résultats dans un JSON
    result = extraire_verbe_et_sujet(phrase)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
