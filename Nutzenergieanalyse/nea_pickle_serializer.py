from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_abschnitt_data_factory import NEAAbschnittDataFactory
from Nutzenergieanalyse.nea_abschnitt_dataframes import NEAAbschnittDataframes
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_file import NEAFile
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor
from Nutzenergieanalyse.nea_serialization_folder_factory import NEASerializationFolderFactory


class NEAPickleSerializer:
    def __init__(self, folder_factory: NEASerializationFolderFactory, abschnitte: list[NEAAbschnitt],
                 sektoren: list[NEASektor], bereiche: list[NEABereich]):
        self.__abschnitte = abschnitte
        self.__sektoren = sektoren
        self.__bereiche = bereiche
        self.__folder_factory = folder_factory

    def __pickle_nea_dataframes(self, dataframes: NEAAbschnittDataframes, land: NEALand, abschnitt: NEAAbschnitt,
                                sektoren: list[NEASektor], bereiche: list[NEABereich]):
        for sektor, bereich, dataframe in dataframes.get_enum(sektoren, bereiche):
            ser_path = self.__folder_factory.create(land, abschnitt, sektor)
            ser_path.mkdir(parents=True, exist_ok=True)
            dataframe.to_pickle(ser_path / f'{bereich.name}.pkl')

    def run(self, files: list[NEAFile]):
        for file in files:
            print(f'Starting {file.land.name}')
            factory = NEAAbschnittDataFactory(self.__sektoren, self.__bereiche)
            for abschnitt in self.__abschnitte:
                data = factory.create(file, abschnitt)
                dic = data.create_dict(abschnitt.jahre)
                dataframes = dic.create_dataframes(abschnitt)
                self.__pickle_nea_dataframes(dataframes, file.land, abschnitt, self.__sektoren, self.__bereiche)
