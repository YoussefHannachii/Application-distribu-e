module MonModule {
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

    interface MonInterface {
        Song getSongByTitle(string title) throws SongNotFoundException;
        Song getSongByArtist(string artist) throws SongNotFoundException;
        string streamAudio(string songPath);
        string streamAudioWithTitle(string titreExtraitAvecNlp) throws SongNotFoundException;
    };
};
