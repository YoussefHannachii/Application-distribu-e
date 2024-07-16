const express = require('express');
const app = express();
const ModuleAndroid= require("./serviceStreamingPourAppAndroid").StreamingAndroid;
const Ice = require("ice").Ice;
const multer = require('multer');
const cors = require('cors');
const fs = require('fs');
const bodyParser = require('body-parser');


app.use(bodyParser.json());


app.use(cors()); 

async function streamAudio(titreExtraitAvecNlp){
    let communicator;
    try {
        communicator = Ice.initialize();
        const base = communicator.stringToProxy("InterfaceStreamingAndroid:default -p 10008");
        const monInterface = await ModuleAndroid.InterfaceStreamingAndroidPrx.checkedCast(base);
        if (monInterface) {
            const audioStream = await monInterface.streamAudioWithTitle(titreExtraitAvecNlp);
            return audioStream;
        } else {
            console.log("Invalid proxy");
            return null;  // Ou une valeur par défaut en cas d'erreur
        }
    } catch (ex) {
        console.log("error here ");
        console.log(ex.toString());
        throw ex;  // Vous pouvez gérer l'exception ou la relancer selon vos besoins
    } finally {
        if (communicator) {
            await communicator.destroy();
        }
    }
  }

  app.post('/testStreamWithTitle', async(req,res) => {
    try {
        const title = req.body.title;
        const urlStream = await streamAudio(title);
        res.json({ 'URL Stream': urlStream });
    } catch (error) {
        console.error(error);
        res.status(500).json({ success: false, error: 'Internal Server Error' });
    }
  });

const port = 3000;
app.listen(port, () => {
    console.log(`Serveur écoutant sur le port ${port}`);
});
