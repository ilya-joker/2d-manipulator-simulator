import math

from manipulator.math_utils import  is_reachable


def find_angles(x, y, link1, link2):
    if not is_reachable(x,y,link1,link2):
        return None
    else:

        alpha = math.acos((x ** 2 + y ** 2 - link1 ** 2 - link2 ** 2) / (2 * link1 * link2))

        gamma = math.atan2(
            link2 * math.sin(alpha),
            link1 + link2 * math.cos(alpha)
        )

        beta = math.atan2(y, x) - gamma

        angle_1_link = beta
        angle_2_link = alpha

        return angle_1_link, angle_2_link

