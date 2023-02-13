'''
Lancer pour executer les tests.
'''

from src import *
from tests import test_utilites, test_algorithmes
import unittest

suite = unittest.TestSuite()
suite.addTest(test_algorithmes.TestVerifications("test_verifie_connexite"))
runner = unittest.TextTestRunner()
runner.run(suite)

print("TESTS ALGORITHMES:")
unittest.main(module=test_algorithmes)

print("TESTS UTILITES:")
unittest.main(module=test_utilites)