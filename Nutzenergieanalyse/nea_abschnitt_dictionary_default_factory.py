from Domain.Nutzenergieanalyse import NEAJahr, NEASektor, NEABereich, NEAAbschnittDictionary, \
    NEAAbschnittDictionaryFactory, NEADataField


class NEAAbschnittDictionaryDefaultFactory(NEAAbschnittDictionaryFactory):
    @staticmethod
    def __create_energietraeger_dict(j: NEAJahr, s: NEASektor, data_fields: list[NEADataField]):
        return {d.energietraeger: d.data for d in data_fields if d.jahr == j and d.sektor == s}

    def __create_sektor_dict(self, j: NEAJahr, sektoren: list[NEASektor], data_fields: list[NEADataField]):
        return {sektor: self.__create_energietraeger_dict(j, sektor, data_fields) for sektor in sektoren}

    def create(self, jahre: list[NEAJahr], sektoren: list[NEASektor], bereiche: list[NEABereich],
               data_fields: list[NEADataField]) -> NEAAbschnittDictionary:
        return {jahr: self.__create_sektor_dict(jahr, sektoren, data_fields) for jahr in jahre}
