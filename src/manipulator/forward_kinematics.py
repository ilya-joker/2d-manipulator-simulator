# Это главный файл логики модели.
#
# Тут живёт объект, который:
#
# содержит два звена,
# содержит два угла,
# умеет вычислять положение конца манипулятора.
#
# Это уже “сердце” проекта.
from manipulator.math_utils import projection

def first_link_end(link_length, angle):
    """
    Calculate the endpoint of the first link.

    Args:
        link_length: Length of the first link.
        angle: Angle of the first joint in degrees.

    Returns:
        Tuple (x, y) — coordinates of the first link endpoint.
    """
    x,y = projection(link_length, angle)
    return x,y

def second_link_end(link_1_length, link_2_length, angle1, angle2):
    """
    Calculate the endpoint of the second link (end effector position).

    Args:
        link_1_length: Length of the first link.
        link_2_length: Length of the second link.
        angle1: Angle of the first joint in degrees.
        angle2: Angle of the second joint relative to first link, in degrees.

    Returns:
        Tuple (x, y) — coordinates of the end effector.
    """
    x1, y1 = first_link_end(link_1_length,angle1)
    x2, y2 = projection(link_2_length, angle1 + angle2)
    x = x1 + x2
    y = y1 + y2
    return x,y

