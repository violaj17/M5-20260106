import unittest
from calculator import Calculator   # Import Calculator class from calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        answer = self.calc.get_sum()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(self.calc.get_sum(), 10, "The answer wasn't 10")

    def test_difference(self):
        answer = self.calc.get_difference()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(self.calc.get_difference(), 6, "The answer wasn't 6")

    def test_product(self):
        answer = self.calc.get_product()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(self.calc.get_product(), 16, "The answer wasn't 16")
    
    def test_quotient(self):
        answer = self.calc.get_quotient()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(self.calc.get_quotient(), 4, "The answer wasn't 4")

if __name__ == "__main__":
    unittest.main()
