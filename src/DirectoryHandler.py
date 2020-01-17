import os
from typing import Set


class DirectoryHandler(object):
    def __init__(self, directory_path):
        self.directory = directory_path

    def directory_exists(self) -> bool:
        """
            Check if the given directory exists in the file system.
        """
        return os.access(self.get_directory(), os.R_OK)

    def get_files(self) -> Set[str]:
        """
            Get the files inside of the specified directory.
        """
        pass

    def create_duplicates_directory(self) -> None:
        """
            Create a new directory to place duplicate files into.
        """
        pass

    def place_files_in_duplicates_directory(self, files:Set[str]) -> None:
        """
            Move duplicate files to the duplicate directory.
        """
        pass
    
    @staticmethod
    def remove_files(files:Set[str]) -> None:
        """
            Remove the specified files from the file system.
        """
        pass

    def get_directory(self):
        """
            Getter method for directory class attribute.
        """
        return self.directory