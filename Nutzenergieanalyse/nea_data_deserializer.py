from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_abschnitt_data_factory import NEAAbschnittDataFactory
from Nutzenergieanalyse.nea_data import NEAData
from Nutzenergieanalyse.nea_file import NEAFile


class NEADataDeserializer:
    def __init__(self, abschnitte: list[NEAAbschnitt], factory: NEAAbschnittDataFactory):
        self.__abschnitte = abschnitte
        self.__factory = factory

    def __load(self, file: NEAFile, abschnitt: NEAAbschnitt):
        data = self.__factory.create(file, abschnitt)
        dic = data.create_dict(abschnitt.jahre)
        return dic.create_dataframes(abschnitt)

    def run(self, files: list[NEAFile]) -> NEAData:
        laender = list([file.land for file in files])
        return NEAData(laender, self.__abschnitte, self.__factory.sektoren, self.__factory.bereiche,
                       {file.land: {abschnitt: self.__load(file, abschnitt) for abschnitt in self.__abschnitte} for file
                        in files})
