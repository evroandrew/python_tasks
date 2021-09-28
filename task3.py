from math import sqrt

MSG_NEXT = 'To add new triangle print "yes"/"y"'
MSG_INFO = 'Enter triangle name and three sides separated by commas.'


class Triangle:
    """
    The main task of this class is to create triangle.
    """

    def __init__(self, triangle_name, side_a, side_b, side_c):
        self.name = triangle_name
        self.side_a = float(side_a)
        self.side_b = float(side_b)
        self.side_c = float(side_c)

    # The area of a triangle is calculated using Heron's formula
    @property
    def square(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = sqrt(p * (p - self.side_a) *
                    (p - self.side_b) * (p - self.side_c))
        return area

    @property
    def triangle_representation(self):
        return self.name, self.square  # check if a triangle with such sides can exist

    @staticmethod
    def is_triangle(sides):
        # check if a triangle with such sides can exist
        for side in sides:
            if side <= 0:
                return False
        side_3 = max(sides)
        sides.remove(side_3)
        side_1, side_2 = sides
        if side_1 + side_2 >= side_3:
            return True
        return False

    @staticmethod
    def show_triangles(triangles):
        # displaying triangles in descending order of their area
        msg_result_none = "No triangles in the list."
        triangles_list = '============= Triangles list: ==============='
        new_line = '\n'
        if len(triangles) == 0:
            return msg_result_none
        else:
            for number, triangle in enumerate(sorted(triangles, key=lambda item: -item[1])):
                triangles_list = f'{triangles_list}{new_line}{number + 1}. [Triangle {triangle[0]}]: {round(triangle[1], 6)} cm'
            return triangles_list


def main():
    triangles = []
    while True:
        try:
            triangle_params = input(MSG_INFO).split(',')
            if len(triangle_params) != 4 or any(float(side) < 0 for side in triangle_params[1:]):
                raise ValueError
        except ValueError:
            print(MSG_INFO)
            continue
        triangle_params[1], triangle_params[2], triangle_params[3] = float(
            triangle_params[1]), float(triangle_params[2]), float(triangle_params[3])
        if Triangle.is_triangle([triangle_params[1], triangle_params[2], triangle_params[3]]):
            triangle = Triangle(triangle_params[0], triangle_params[1], triangle_params[2], triangle_params[3])
            triangles.append(triangle.triangle_representation)
        else:
            print(
                f'Triangle with such sides ({triangle_params[1]}, {triangle_params[2]}, {triangle_params[3]}) does '
                f'not exist')
        answer_next = input(MSG_NEXT).lower()
        if answer_next not in ['yes', 'y']:
            break
    print(Triangle.show_triangles(triangles))


if __name__ == '__main__':
    main()
