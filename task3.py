from math import sqrt
from Validation import Validation

msg_next = 'To add new triangle print "yes"/"y"'
msg_info = 'Enter triangle name and three sides separated by commas.'
msg_result_none = "No triangles in the list."


class Triangle:
    def __init__(self, triangle_name, side_a, side_b, side_c):
        self.name = triangle_name
        self.side_a = float(side_a)
        self.side_b = float(side_b)
        self.side_c = float(side_c)

    @property
    def square(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = sqrt(p * (p - self.side_a) *
                    (p - self.side_b) * (p - self.side_c))
        return area


def triangle_may_exist(sides):
    side_3 = max(sides)
    sides.remove(side_3)
    side_1, side_2 = sides
    if side_1 + side_2 > side_3:
        return True
    return False


def show_triangles(triangles):
    print('============= Triangles list: ===============')
    if type(triangles) == str:
        print(triangles)
    else:
        for number, triangle in enumerate(sorted(triangles, key=lambda item: -item[1])):
            print(
                f'{number + 1}. [Triangle {triangle[0]}]: {round(triangle[1], 6)} cm')


if __name__ == '__main__':
    triangles = []
    while True:
        try:
            triangle_params = input(msg_info).split(',')
            Validation.triangle_arguments_validation(triangle_params)
        except ValueError:
            print(msg_info)
            continue
        triangle_params[1], triangle_params[2], triangle_params[3] = float(
            triangle_params[1]), float(triangle_params[2]), float(triangle_params[3])
        if triangle_may_exist([triangle_params[1], triangle_params[2], triangle_params[3]]):
            triangle = Triangle(triangle_params[0].strip(
            ), triangle_params[1], triangle_params[2], triangle_params[3])
            triangles.append((triangle.name, triangle.square))
        else:
            print(
                f'Triangle with such sides ({triangle_params[1]}, {triangle_params[2]}, {triangle_params[3]}) does '
                f'not exist')
        answer_next = input(msg_next).lower()
        if answer_next != 'yes' and answer_next != 'y':
            break
    if len(triangles) > 0:
        show_triangles(triangles)
    else:
        show_triangles(msg_result_none)
