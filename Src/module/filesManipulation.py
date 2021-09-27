import os

class FolderAndFiles:

    def __init__(self, path: str) -> None:
        self.path = path

    def createFolder(self, path: str):
        try:
            os.makedirs(path)
        except FileExistsError:
            pass