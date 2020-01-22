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

    @mock.patch("os.path.isfile", return_value=True)
    def test_get_files_correct(self, mock_isfile):
        """
            Ensure get_files returns the correct files for given directory.
        """
        mock_files = ["file1", "file2"]
        os.listdir = mock.MagicMock(return_value=mock_files)
        self.directory_handler.directory_exists = mock.MagicMock(return_value=True)
        requested_files = self.directory_handler.get_files()

        self.assertEqual(requested_files, set(mock_files))

    def test_get_files_dir_not_exists(self):
        """
            Ensure get_files returns an empty set when the directory
            does not exist.
        """
        self.directory_handler.directory_exists = mock.MagicMock(return_value=False)
        requested_files = self.directory_handler.get_files()

        self.assertEqual(requested_files, set())
        
# DirectoryHandler.create_duplicates_directory test cases

    @mock.patch("os.mkdir")
    def test_create_dups_dir_correct(self, mock_mkdir):
        """
            Ensure the duplicate directory is successfully
            created.
        """
        dups_path = os.path.join(self.directory_handler.get_directory(), "duplicates")
        self.directory_handler.create_duplicates_directory()
        
        mock_mkdir.assert_called_once_with(dups_path)


# DirectoryHandler.place_files_in_duplicates_directory test cases

    @mock.patch("os.replace")
    def test_place_files_not_called_when_no_duplicates(self, mock_patch):
        """
            Ensure os.replace is not called when there are no duplicate files.
        """
        dup_files = {}
        self.directory_handler.place_files_in_duplicates_directory(dup_files)

        mock_patch.assert_not_called()


    @mock.patch("os.replace")
    def test_place_files_calls_replace(self, mock_replace):
        """
            Ensure os.replace is called with the correct file paths.
        """
        dup_file = "file1.txt"
        dup_file_dir = os.path.join(self.directory_handler.get_directory(), dup_file)
        new_dir = os.path.join(self.directory_handler.get_directory(),"duplicates", dup_file)
        self.directory_handler.place_files_in_duplicates_directory({dup_file})

        mock_replace.assert_called_once_with(dup_file_dir, new_dir)
