from Domain.Energiebilanz import EBSektor
from Domain.Energiebilanz.eb_datafield import EBDataField
from Energiebilanz.eb_file_dictionary import EBFileDictionary


class EBFileDictionaryFactory:
    @staticmethod
    def __create_energietraeger_dict(s: EBSektor, data_fields: list[EBDataField]):
        return {d.energietraeger: d.data for d in data_fields if d.sektor == s}

    def create(self, sektoren: list[EBSektor], data_fields: list[EBDataField]) -> EBFileDictionary:
        return {sektor: self.__create_energietraeger_dict(sektor, data_fields) for sektor in sektoren}
