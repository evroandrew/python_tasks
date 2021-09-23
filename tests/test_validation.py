import unittest
from Validation import Validation


class TestValidation(unittest.TestCase):
    """
    This class tests Validation.py
    """

    def test_positive_float_validation(self):
        V = Validation()
        self.assertEqual(V.positive_float_validation('2'), 2)
        self.assertEqual(V.positive_float_validation('2.2'), 2.2)
        self.assertRaises(ValueError, V.positive_float_validation, 'abc')
        self.assertRaises(ValueError, V.positive_float_validation, '')
        self.assertRaises(ValueError, V.positive_float_validation, '-2')
        self.assertRaises(ValueError, V.positive_float_validation, '-2.2')

    def test_positive_integer_validation(self):
        V = Validation()
        self.assertEqual(V.positive_integer_validation('2'), 2)
        self.assertRaises(ValueError, V.positive_integer_validation, 'abc')
        self.assertRaises(ValueError, V.positive_integer_validation, '')
        self.assertRaises(ValueError, V.positive_integer_validation, '-2')
        self.assertRaises(ValueError, V.positive_integer_validation, '-2.2')
        self.assertRaises(ValueError, V.positive_integer_validation, '2.2')


if __name__ == '__main__':
    unittest.main()
