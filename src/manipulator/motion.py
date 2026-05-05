import math

from manipulator.forward_kinematics import second_link_end, first_link_end

def generate_angle_path(start_angle_1_deg, start_angle_2_deg, target_angle_1_deg, target_angle_2_deg, steps):
    """
    Generate a linear interpolation path between start and target joint angles.

    Args:
        start_angle_1_deg: Starting angle of joint 1 in degrees.
        start_angle_2_deg: Starting angle of joint 2 in degrees.
        target_angle_1_deg: Target angle of joint 1 in degrees.
        target_angle_2_deg: Target angle of joint 2 in degrees.
        steps: Number of interpolation steps. Total points = steps + 1.

    Returns:
        List of tuples [(angle_1, angle_2), ...] with steps + 1 entries.

    Raises:
        TypeError: If steps is not an integer.
        ValueError: If steps is not greater than 0.
    """
    if not isinstance(steps, int):
        raise TypeError("steps must be an integer")

    if steps <= 0:
        raise ValueError("steps must be greater than 0")

    angle_step_1 = (target_angle_1_deg-start_angle_1_deg) / steps
    angle_step_2 = (target_angle_2_deg - start_angle_2_deg) / steps

    angles_of_motion = []

    for i in range(steps + 1):
        new_angle_1 = start_angle_1_deg + angle_step_1 * i
        new_angle_2 = start_angle_2_deg + angle_step_2 * i

        angles_of_motion.append((new_angle_1, new_angle_2))

    return angles_of_motion

def generate_position_path(angle_path_deg, link_1_length, link_2_length):
    """
    Convert a path of joint angles into a path of manipulator positions.

    Args:
        angle_path_deg: List of (angle_1_deg, angle_2_deg) tuples.
        link_1_length: Length of the first link.
        link_2_length: Length of the second link.

    Returns:
        List of tuples [(first_point, second_point), ...] where each point is (x, y).
    """
    position_path = []

    for angle_1_deg, angle_2_deg in angle_path_deg:
        first_point = first_link_end(link_1_length, angle_1_deg)

        second_point = second_link_end(
            link_1_length,
            link_2_length,
            angle_1_deg,
            angle_2_deg
        )

        position_path.append((first_point, second_point))

    return position_path
