'''
Lancer pour executer les tests.
'''

from src import utilites
from tests import test_utilites, test_algorithmes
import unittest

print("TESTS ALGORITHMES:")
unittest.main(module=test_algorithmes)