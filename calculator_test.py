from unittest import  TestCase, main
from calculator import calculator

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'),4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_multi(self):
        self.assertEqual(4*4, 16)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

if __name__ == '__main__':
    main()