module StreamingAndroid {
    struct Song {
        string title;
        string artist;
        string type;
        string dateofrelease;
        string emplacement;
    };

    exception SongNotFoundException {
        string reason;
    };

    interface InterfaceStreamingAndroid {
        string streamAudioWithTitle(string titreExtraitAvecNlp) throws SongNotFoundException;
    };
};
