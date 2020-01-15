import unittest
from test_FileHasher import TestFileHasher

def test_suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestFileHasher))
    return test_suite

my_test_suite = test_suite()
runner=unittest.TextTestRunner()
runner.run(my_test_suite)