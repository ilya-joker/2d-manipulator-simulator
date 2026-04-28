import math

from config import LINK_1_LENGTH, LINK_2_LENGTH, DEFAULT_ANGLE_1, DEFAULT_ANGLE_2
from manipulator.math_utils import distance
from manipulator.visualizer import visualize_manipulator
from forward_kinematics import first_link_end, second_link_end
from printer import print_manipulator_state
from inverse_kinematics import find_angles

def main():
    while True:
        x_input = input("Enter target x or q to quit: ")

        if x_input == "q":
            print("Exit")
            break

        y_input = input("Enter target y: ")

        x = float(x_input)
        y = float(y_input)

        angles = find_angles(x, y, LINK_1_LENGTH, LINK_2_LENGTH)

        if angles is None:
            print("Target is unreachable")
            continue

        a, b = angles

        angle_1_link = math.degrees(a)
        angle_2_link = math.degrees(b)

        first_point = first_link_end(LINK_1_LENGTH, angle_1_link)

        second_point = second_link_end(
            LINK_1_LENGTH,
            LINK_2_LENGTH,
            angle_1_link,
            angle_2_link
        )

        print_manipulator_state(
            LINK_1_LENGTH,
            LINK_2_LENGTH,
            angle_1_link,
            angle_2_link,
            first_point,
            second_point
        )

        target_point = (x, y)
        error = distance(target_point, second_point)

        print(f"Target point: {target_point}")
        print(f"End effector: {second_point}")

        if error < 1e-6:
            print("IK check: OK")
        else:
            print("IK check: FAILED")

        visualize_manipulator(first_point, second_point, target_point)

if __name__ == "__main__":
    main()