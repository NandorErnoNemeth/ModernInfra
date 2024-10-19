import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_operations(self):
        result = self.calc.add(1, 2)
        result = self.calc.multiply(result, 3)
        result = self.calc.subtract(result, 4)
        result = self.calc.divide(result, 2)
        self.assertEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()
