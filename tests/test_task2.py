import unittest
import task2


class Test_Envelope_Compare(unittest.TestCase):
    """
    This class tests task2.py
    """

    def test_representation(self):
        env1 = task2.Envelope(1, 1)
        env2 = task2.Envelope(2, 2)
        env3 = task2.Envelope(0, 2)
        self.assertEqual((task2.Envelope.env_compare(env1, env1)),
                         'No envelope fits inside another. Envelope are the same.')
        self.assertEqual((task2.Envelope.env_compare(env3, env1)), 'No envelope fits inside another.')
        self.assertEqual((task2.Envelope.env_compare(env1, env2)), 'The first envelope fits into the second.')
        self.assertEqual((task2.Envelope.env_compare(env2, env1)), 'The second envelope fits into the first.')


if __name__ == '__main__':
    unittest.main()
