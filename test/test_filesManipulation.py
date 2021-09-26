import os

class FolderAndFiles:

    def __init__(self, path: str) -> None:
        self.path = path

    def createFolder(self, folder_name: str) -> None:
        """Creates folder in default path.

        Args:
            folder_name (str): Folder's Name
            return: None
        """
        path = f'{self.path}\{folder_name}'
        try:
            os.makedirs(path)
        except FileExistsError:
            print(f'Está pasta já existe')
    
