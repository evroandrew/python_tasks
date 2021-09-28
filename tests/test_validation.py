import unittest
from _validator import Validator


class TestValidation(unittest.TestCase):
    """
    This class tests _validator.py
    """

    def test_positive_float_validation(self):
        validator = Validator()
        self.assertEqual(validator.positive_float_validation('2'), 2)
        self.assertEqual(validator.positive_float_validation('2.2'), 2.2)
        self.assertRaises(ValueError, validator.positive_float_validation, 'abc')
        self.assertRaises(ValueError, validator.positive_float_validation, '')
        self.assertRaises(ValueError, validator.positive_float_validation, '-2')
        self.assertRaises(ValueError, validator.positive_float_validation, '-2.2')

    def test_positive_integer_validation(self):
        validator = Validator()
        self.assertEqual(validator.positive_integer_validation('2'), 2)
        self.assertRaises(ValueError, validator.positive_integer_validation, 'abc')
        self.assertRaises(ValueError, validator.positive_integer_validation, '')
        self.assertRaises(ValueError, validator.positive_integer_validation, '-2')
        self.assertRaises(ValueError, validator.positive_integer_validation, '-2.2')
        self.assertRaises(ValueError, validator.positive_integer_validation, '2.2')


if __name__ == '__main__':
    unittest.main()
