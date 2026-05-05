import math

from manipulator.config import DEFAULT_ANGLE_1, DEFAULT_ANGLE_2
from manipulator.forward_kinematics import first_link_end, second_link_end
from manipulator.inverse_kinematics import find_angles


class TwoLinkManipulator:
    """
    Represents a 2-link planar robotic manipulator.

    Stores the current joint angles and link lengths.
    Provides methods for forward kinematics, inverse kinematics,
    and moving to a target point.

    Attributes:
        link_1_length: Length of the first link.
        link_2_length: Length of the second link.
        current_angle_1_deg: Current angle of the first joint in degrees.
        current_angle_2_deg: Current angle of the second joint in degrees.
    """
    def __init__(self, link_1_length, link_2_length):
        """
        Initialize the manipulator with given link lengths.
        Starting angles are taken from config defaults.

        Args:
            link_1_length: Length of the first link.
            link_2_length: Length of the second link.
        """
        self.link_1_length = link_1_length
        self.link_2_length = link_2_length
        self.current_angle_1_deg = DEFAULT_ANGLE_1
        self.current_angle_2_deg = DEFAULT_ANGLE_2

    def get_position(self):
        """
        Calculate current positions of both link endpoints using forward kinematics.

        Returns:
            Tuple (first_point, second_point) where each point is (x, y).
        """
        first_point = first_link_end(self.link_1_length, self.current_angle_1_deg)
        second_point = second_link_end(self.link_1_length, self.link_2_length, self.current_angle_1_deg, self.current_angle_2_deg)
        return first_point, second_point

    def move_to(self, target_point, elbow):
        """
        Move the manipulator to a target point using inverse kinematics.
        Updates current joint angles if the target is reachable.

        Args:
            target_point: Tuple (x, y) — target coordinates.
            elbow: Elbow mode, 'up' or 'down'.

        Returns:
            True if target is reachable and angles were updated.
            False if target is unreachable.
        """
        x, y = target_point
        angles = find_angles(x, y, self.link_1_length, self.link_2_length, elbow)
        if angles is None:
            return False
        angle_1_rad, angle_2_rad = angles
        self.current_angle_1_deg = math.degrees(angle_1_rad)
        self.current_angle_2_deg = math.degrees(angle_2_rad)
        return True

