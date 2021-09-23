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
        msgs = ['No envelope fits inside another. Envelope are the same.',
                'No envelope fits inside another.',
                'The first envelope fits into the second.',
                'The second envelope fits into the first.']
        test_cases = [
            {'arguments': {'envelope1': env1, 'envelope2': env1}, 'excepted_result': msgs[0]},
            {'arguments': {'envelope1': env3, 'envelope2': env1}, 'excepted_result': msgs[1]},
            {'arguments': {'envelope1': env1, 'envelope2': env2}, 'excepted_result': msgs[2]},
            {'arguments': {'envelope1': env2, 'envelope2': env1}, 'excepted_result': msgs[3]},
            {'arguments': {'envelope1': env2, 'envelope2': env3}, 'excepted_result': msgs[1]}
        ]
        for test_case in test_cases:
            self.assertEqual(task2.Envelope.env_compare(**test_case['arguments']), test_case['excepted_result'])


if __name__ == '__main__':
    unittest.main()
