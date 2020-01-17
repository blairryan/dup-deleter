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

# DirectoryHandler.get_files test cases

    def test_get_files_returns_set(self):
        """
            Ensure return type of test_files is a set. 
        """
        requested_files = self.directory_handler.get_files()

        assert isinstance(requested_files, set)

    def test_get_files_correct(self):
        """
            Ensure get_files returns the correct files for given directory.
        """
        mock_files = ["file1", "file2"]
        os.walk = mock.MagicMock()
        os.walk.return_value = ("root", [], mock_files)
        requested_files = self.directory_handler.get_files()

        self.assertEqual(requested_files, set(mock_files))



    