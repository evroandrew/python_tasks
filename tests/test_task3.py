import unittest
import task3


class TestTriangle(unittest.TestCase):
    """
    This class tests task3.py
    """

    def test_Triangle_square(self):
        self.assertEqual(task3.Triangle('', 3, 4, 5).square, 6.0)
        self.assertEqual(task3.Triangle('', 1, 2, 2).square, 0.9682458365518543)
        self.assertEqual(task3.Triangle('', 3, 3, 3).square, 3.897114317029974)

    def test_triangle_may_exist(self):
        self.assertTrue(task3.Triangle.is_triangle([3, 4, 5]))
        self.assertTrue(task3.Triangle.is_triangle([1, 2, 2]))
        self.assertTrue(task3.Triangle.is_triangle([3, 3, 3]))
        self.assertTrue(task3.Triangle.is_triangle([1, 1, 2]))

        self.assertFalse(task3.Triangle.is_triangle([1, 1, 0]))
        self.assertFalse(task3.Triangle.is_triangle([1, 1, 7]))
        self.assertFalse(task3.Triangle.is_triangle([-1, 1, 2]))

    def test_triangle_representation(self):
        self.assertEqual(task3.Triangle('a', 3, 4, 5).triangle_representation, ('a', 6.0))
        self.assertEqual(task3.Triangle('b', 1, 2, 2).triangle_representation, ('b', 0.9682458365518543))
        self.assertEqual(task3.Triangle('c', 3, 3, 3).triangle_representation, ('c', 3.897114317029974))

    def test_show_triangles(self):
        triangle1 = task3.Triangle('a', 3, 4, 5)
        triangle2 = task3.Triangle('b', 1, 2, 2)
        triangle3 = task3.Triangle('c', 3, 3, 3)
        triangle1_repr = '[Triangle a]: 6.0 cm'
        triangle2_repr = '[Triangle b]: 0.968246 cm'
        triangle3_repr = '[Triangle c]: 3.897114 cm'
        triangles_list = '============= Triangles list: ==============='
        new_line = '\n'

        test_cases = [
            {'arguments': {'triangles': [triangle1.triangle_representation, triangle2.triangle_representation]},
             'excepted_result': f'{triangles_list}{new_line}1. {triangle1_repr}{new_line}2. {triangle2_repr}'},
            {'arguments': {'triangles': [triangle2.triangle_representation, triangle3.triangle_representation]},
             'excepted_result': f'{triangles_list}{new_line}1. {triangle3_repr}{new_line}2. {triangle2_repr}'},
            {'arguments': {'triangles': [triangle1.triangle_representation, triangle3.triangle_representation]},
             'excepted_result': f'{triangles_list}{new_line}1. {triangle1_repr}{new_line}2. {triangle3_repr}'},
            {'arguments': {'triangles': [triangle2.triangle_representation, triangle3.triangle_representation,
                                         triangle1.triangle_representation]},
             'excepted_result': f'{triangles_list}{new_line}1. {triangle1_repr}{new_line}2. {triangle3_repr}{new_line}3. {triangle2_repr}'},
            {'arguments': {'triangles': []}, 'excepted_result': 'No triangles in the list.'},
        ]
        for test_case in test_cases:
            self.assertEqual(task3.Triangle.show_triangles(**test_case['arguments']), test_case['excepted_result'])


if __name__ == '__main__':
    unittest.main()
