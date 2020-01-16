import unittest
import hashlib
from unittest import mock
from DirectoryHandler import DirectoryHandler
import os

class TestDirectoryHandler(unittest.TestCase):
    def setUp(self):
        self.directory_handler = DirectoryHandler("fake dir path")

# DirectoryHandler.directory_exists test cases

    def test_directory_exists_returns_bool(self):
        """
            Ensure the return type of directory_exists is of type bool.
        """
        dir_exists = self.directory_handler.directory_exists()
        assert isinstance(dir_exists, bool)

    def test_directory_not_exists_(self):
        """
            Ensure directory_exists returns False when the 
            directory does not exist.
        """
        dir_exists = self.directory_handler.directory_exists()

        self.assertFalse(dir_exists)

    def test_directory_exists(self):
        """
            Ensure directory_exists returns True when the directory exists.
        """
        self.directory_handler.get_directory = mock.MagicMock()
        self.directory_handler.get_directory.return_value = os.getcwd()
        dir_exists = self.directory_handler.directory_exists()

        self.assertTrue(dir_exists)





    