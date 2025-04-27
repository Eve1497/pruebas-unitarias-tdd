# tests/test_calculadora.py

import unittest
from src.calculadora import sumar, restar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 4), -4)

if __name__ == '__main__':
    unittest.main()
