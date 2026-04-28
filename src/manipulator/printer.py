# Это файл для красивого вывода.
#
# Например:
#
# вывести текущее состояние
# вывести длины
# вывести углы
# вывести координаты

def print_manipulator_state(link_1_length, link_2_length, angle1, angle2, first_point, second_point):
    x1, y1 = first_point
    x2, y2 = second_point

    print("Manipulator state:")
    print(f"Link 1 length: {link_1_length}")
    print(f"Link 2 length: {link_2_length}")
    print(f"Angle 1: {angle1} degrees")
    print(f"Angle 2: {angle2} degrees")
    print()
    print(f"First link end: ({x1:.3f}, {y1:.3f})")
    print(f"Second link end: ({x2:.3f}, {y2:.3f})")