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
        self.assertTrue(task3.triangle_may_exist([3, 4, 5]))
        self.assertTrue(task3.triangle_may_exist([1, 2, 2]))
        self.assertTrue(task3.triangle_may_exist([3, 3, 3]))
        self.assertFalse(task3.triangle_may_exist([1, 1, 2]))

    def test_triangle_representation(self):
        self.assertEqual(task3.Triangle('a', 3, 4, 5).triangle_representation, ('a', 6.0))
        self.assertEqual(task3.Triangle('b', 1, 2, 2).triangle_representation, ('b', 0.9682458365518543))
        self.assertEqual(task3.Triangle('c', 3, 3, 3).triangle_representation, ('c', 3.897114317029974))

    def test_show_triangles(self):
        triangle1 = task3.Triangle('a', 3, 4, 5)
        triangle2 = task3.Triangle('b', 1, 2, 2)
        triangle3 = task3.Triangle('c', 3, 3, 3)
        triangles_list = '============= Triangles list: ==============='
        self.assertEqual(task3.show_triangles([triangle1.triangle_representation, triangle2.triangle_representation]),
                         [triangles_list, '1. [Triangle a]: 6.0 cm', '2. [Triangle b]: 0.968246 cm'])
        self.assertEqual(task3.show_triangles([triangle2.triangle_representation, triangle3.triangle_representation]),
                         [triangles_list, '1. [Triangle c]: 3.897114 cm', '2. [Triangle b]: 0.968246 cm'])
        self.assertEqual(task3.show_triangles([triangle1.triangle_representation, triangle3.triangle_representation]),
                         [triangles_list, '1. [Triangle a]: 6.0 cm', '2. [Triangle c]: 3.897114 cm'])
        self.assertEqual(task3.show_triangles(
            [triangle2.triangle_representation, triangle3.triangle_representation, triangle1.triangle_representation]),
            [triangles_list, '1. [Triangle a]: 6.0 cm', '2. [Triangle c]: 3.897114 cm', '3. [Triangle b]: 0.968246 cm'])
        self.assertEqual(task3.show_triangles([]), 'No triangles in the list.')


if __name__ == '__main__':
    unittest.main()
