import math

from manipulator.config import LINK_1_LENGTH, LINK_2_LENGTH
from manipulator.math_utils import distance
from manipulator.motion import generate_angle_path, generate_position_path
from manipulator.visualizer import visualize_motion_path
from manipulator.forward_kinematics import first_link_end, second_link_end
from manipulator.printer import print_manipulator_state
from manipulator.inverse_kinematics import find_angles

def main():

    x = float(input("Enter target x: "))
    y = float(input("Enter target y: "))
    elbow_input = input("Choose elbow mode [up/down] (default: up): ").strip().lower()

    if elbow_input == "":
        elbow = "up"
    elif elbow_input in ["up", "down"]:
        elbow = elbow_input
    else:
        print("Invalid elbow mode. Use 'up' or 'down'.")
        return

    angles = find_angles(x, y, LINK_1_LENGTH, LINK_2_LENGTH, elbow=elbow)

    if angles is None:
        print("Target is unreachable")
        return

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

    print(f"Target point: {target_point}")
    print(f"End effector: {second_point}")

    error = distance(target_point, second_point)
    if error < 1e-6:
        print("IK check: OK")
    else:
        print("IK check: FAILED")

    start_angle_1_deg = 0
    start_angle_2_deg = 0
    motion_steps = 5

    angle_path = generate_angle_path(
        start_angle_1_deg=start_angle_1_deg,
        start_angle_2_deg=start_angle_2_deg,
        target_angle_1_deg=angle_1_link,
        target_angle_2_deg=angle_2_link,
        steps=motion_steps
    )

    position_path = generate_position_path(
        angle_path,
        LINK_1_LENGTH,
        LINK_2_LENGTH
    )

    visualize_motion_path(
        position_path,
        LINK_1_LENGTH,
        LINK_2_LENGTH,
        target_point
    )

if __name__ == "__main__":
    main()