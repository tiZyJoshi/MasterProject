from Domain.Nutzenergieanalyse import NEAFile, NEAAbschnitt, NEASektor, NEABereich, NEAAbschnittDataFactory, \
    NEAAbschnittDataframesFactory, NEAAbschnittDictionaryFactory, NEAData, NEADataFactory, NEAFilesFactory


class NEADataNewFactory(NEADataFactory):
    def __init__(self,
                 files_factory: NEAFilesFactory,
                 data_factory: NEAAbschnittDataFactory,
                 dictionary_factory: NEAAbschnittDictionaryFactory,
                 dataframes_factory: NEAAbschnittDataframesFactory):
        self.__files_factory = files_factory
        self.__data_factory = data_factory
        self.__dictionary_factory = dictionary_factory
        self.__dataframes_factory = dataframes_factory

    def __load(self, file: NEAFile, abschnitt: NEAAbschnitt, sektoren: list[NEASektor], bereiche: list[NEABereich]):
        abschnitt_data_fields = self.__data_factory.create(file, abschnitt, sektoren, bereiche)
        abschnitt_dictionary = self.__dictionary_factory.create(abschnitt.jahre, sektoren, bereiche,
                                                                abschnitt_data_fields)
        abschnitt_dataframes = self.__dataframes_factory.create(abschnitt, sektoren, bereiche, abschnitt_dictionary)
        return abschnitt_dataframes

    def create(self, abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor],
               bereiche: list[NEABereich]) -> NEAData:
        files = self.__files_factory.create()
        laender = list([file.land for file in files])
        return NEAData(laender, abschnitte, sektoren, bereiche, {
            file.land: {abschnitt: self.__load(file, abschnitt, sektoren, bereiche) for abschnitt in abschnitte} for
            file in files})
