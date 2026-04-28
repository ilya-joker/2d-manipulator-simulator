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

def first_link_end(link_length,angle):
    x,y = projection(link_length, angle)
    return x,y

def second_link_end(link_1_length,link_2_length,angle1,angle2):
    x1, y1 = first_link_end(link_1_length,angle1)
    x2, y2 = projection(link_2_length, angle1 + angle2)
    x = x1 + x2
    y = y1 + y2
    return x,y

