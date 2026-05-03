import math

from manipulator.config import DEFAULT_ANGLE_1, DEFAULT_ANGLE_2
from manipulator.forward_kinematics import first_link_end, second_link_end
from manipulator.inverse_kinematics import find_angles


class TwoLinkManipulator:
    def __init__(self, link_1_length, link_2_length):
        self.link_1_length = link_1_length
        self.link_2_length = link_2_length
        self.current_angle_1_deg = DEFAULT_ANGLE_1
        self.current_angle_2_deg = DEFAULT_ANGLE_2

    def get_position(self):
        first_point = first_link_end(self.link_1_length, self.current_angle_1_deg)
        second_point = second_link_end(self.link_1_length, self.link_2_length, self.current_angle_1_deg, self.current_angle_2_deg)
        return first_point, second_point

    def move_to(self, target_point, elbow):
        x, y = target_point
        angles = find_angles(x, y, self.link_1_length, self.link_2_length, elbow)
        if angles is None:
            return False
        angle_1_rad, angle_2_rad = angles
        self.current_angle_1_deg = math.degrees(angle_1_rad)
        self.current_angle_2_deg = math.degrees(angle_2_rad)
        return True

