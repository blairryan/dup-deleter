import unittest
import hashlib
from FileHasher import FileHasher
from unittest import mock

class TestFileHasher(unittest.TestCase):
    def setUp(self):
        self.hash_instance = FileHasher("file")

    def test_generate_hash_called(self):
        """
            Ensure the generate_hash method is called.
        """
        self.hash_instance.generate_hash = mock.MagicMock()
        
        self.hash_instance.generate_hash()
        self.hash_instance.generate_hash.assert_called_once()

    @mock.patch("builtins.open", new_callable=mock.mock_open())
    @mock.patch("hashlib._hashlib.HASH")
    def test_open_called(self, m_hash, m):
        """
            Ensure the builtin open method is called on the given file.
        """
        self.hash_instance.generate_hash()
        m.assert_called_with("file", "rb")

    @mock.patch("builtins.open", new_callable=mock.mock_open(), return_value="fake data")
    def test_file_hashed(self, mock_open):
        """
            Ensure the return type of generate_hash matches the return type for the hashlib hexdigest method.
        """
        val = self.hash_instance.generate_hash()
        assert isinstance(val, str)