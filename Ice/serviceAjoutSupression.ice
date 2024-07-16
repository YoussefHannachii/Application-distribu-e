module ModuleAjoutSupp {
    interface MonInterface {
        string addSong(string title,string artist,string type,string dateofrelease,string emplacement);
        string deleteSong(string title);
    };
};
