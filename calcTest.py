import unittest

from calc import Interpreter


class SimpleCalcTestCases(unittest.TestCase):

    def test_adding_of_one_digit_numbers(self):
        text = '3+4'
        interpreter = Interpreter(text)
        self.assertEqual(7,
                         interpreter.expr())

    def test_adding_of_two_several_digits_numbers(self):
        text = '12+3'
        interpreter = Interpreter(text)
        self.assertEqual(15,
                         interpreter.expr())

    def test_subtract_of_two_several_digits_numbers(self):
        text = '120-3'
        interpreter = Interpreter(text)
        self.assertEqual(117,
                         interpreter.expr())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(SimpleCalcTestCases('test_adding_of_one_digit_numbers'))
    suite.addTest(SimpleCalcTestCases('test_adding_of_two_several_digits_numbers'))
    suite.addTest(SimpleCalcTestCases('test_subtract_of_two_several_digits_numbers'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())