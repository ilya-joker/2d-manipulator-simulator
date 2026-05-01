# Например:
#
# перевод градусов в радианы
# вычисление координат точки
# вспомогательные формулы

import math

# Calculate cosine. Take deg
def cos(angle):
    return math.cos(math.radians(angle))

# Calculate sine. Take deg
def sin(angle):
    return math.sin(math.radians(angle))

# Endpoint of the first link in world coordinates
def projection(link_length, angle):
    x = link_length * cos(angle)
    y = link_length * sin(angle)
    return x,y


def is_reachable(x,y,link1,link2):
    r = math.sqrt(x ** 2 + y ** 2)
    return abs(link1 - link2) <= r <= link1 + link2

def distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_workspace_bounds(link_1_length,link_2_length):
    outer_radius = link_1_length + link_2_length
    inner_radius = abs(link_1_length - link_2_length)
    return outer_radius, inner_radius




