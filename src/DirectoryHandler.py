import os
from typing import Set


class DirectoryHandler(object):
    def __init__(self, directory_path):
        self.directory = directory_path

    def directory_exists(self, directory: str = None) -> bool:
        """
            Check if the given directory exists in the file system, if no directory
            given, use self.direcotory.
        """
        return os.access(directory if directory else self.get_directory(), os.R_OK)

    def get_files(self) -> Set[str]:
        """
            Get the files inside of the specified directory.
        """
        return ({f for f in os.listdir(self.get_directory())
                    if os.path.isfile(os.path.join(self.get_directory(), f))} if self.directory_exists(self.get_directory()) else set())

    def create_duplicates_directory(self) -> None:
        """
            Create a new directory to place duplicate files into.
        """
        dups_path = os.path.join(self.get_directory(), "duplicates")
        if not self.directory_exists(dups_path): os.mkdir(dups_path)

    def place_files_in_duplicates_directory(self, files: Set[str]) -> None:
        """
            Move duplicate files to the duplicate directory.
        """
        for f in files:
            src = os.path.join(self.get_directory(), f)
            dst = os.path.join(self.get_directory(), "duplicates", f)
            os.replace(src, dst)
    
    def remove_files(self, files: Set[str]) -> None:
        """
            Remove the specified files from the file system.
        """
        for f in files:
            src = os.path.join(self.get_directory(), f)
            os.remove(src)

    def get_directory(self):
        """
            Getter method for directory class attribute.
        """
        return self.directory