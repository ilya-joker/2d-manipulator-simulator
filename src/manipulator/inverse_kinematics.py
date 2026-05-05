import math

from manipulator.math_utils import  is_reachable


def find_angles(x, y, link1, link2, elbow="down"):
    """
    Calculate joint angles to reach target point (x, y).

    Args:
        x: Target x coordinate.
        y: Target y coordinate.
        link1: Length of the first link.
        link2: Length of the second link.
        elbow: Elbow mode, 'up' or 'down' (default: 'down').

    Returns:
        Tuple (angle_1_rad, angle_2_rad) if target is reachable.
        None if target is unreachable.

    Raises:
        ValueError: If elbow is not 'up' or 'down'.
    """
    if not is_reachable(x,y,link1,link2):
        return None
    else:

        alpha = math.acos((x ** 2 + y ** 2 - link1 ** 2 - link2 ** 2) / (2 * link1 * link2))
        if elbow == "up":
            alpha = - alpha
        elif elbow == "down":
            alpha = alpha
        else:
            raise ValueError("elbow must be 'up' or 'down'")
        gamma = math.atan2(
            link2 * math.sin(alpha),
            link1 + link2 * math.cos(alpha)
        )

        beta = math.atan2(y, x) - gamma

        angle_1_link = beta
        angle_2_link = alpha

        return angle_1_link, angle_2_link

