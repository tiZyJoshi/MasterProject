from Nutzenergieanalyse.nea_file import NEAFile
from Nutzenergieanalyse.nea_laender import NEALaender


class NEAFiles:
    def __init__(self, files: list[NEAFile]):
        self.files = files

    def get_laender(self) -> NEALaender:
        return NEALaender([file.land for file in self.files])
