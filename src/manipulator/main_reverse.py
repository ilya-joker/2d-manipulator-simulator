from manipulator.config import LINK_1_LENGTH, LINK_2_LENGTH, DEFAULT_ANGLE_1, DEFAULT_ANGLE_2
from manipulator.math_utils import distance
from manipulator.motion import generate_angle_path, generate_position_path
from manipulator.robot import TwoLinkManipulator
from manipulator.visualizer import animate_motion_path
from manipulator.printer import print_manipulator_state


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

    target_point = (x, y)

    arm = TwoLinkManipulator(LINK_1_LENGTH, LINK_2_LENGTH)

    if not arm.move_to(target_point, elbow): # find th current angles

        print("Target is unreachable")
        return

    first_point,second_point = arm.get_position()

    print_manipulator_state(
        LINK_1_LENGTH,
        LINK_2_LENGTH,
        arm.current_angle_1_deg,
        arm.current_angle_2_deg,
        first_point,
        second_point
    )



    print(f"Target point: {target_point}")
    print(f"End effector: {second_point}")

    error = distance(target_point, second_point)
    if error < 1e-6:
        print("IK check: OK")
    else:
        print("IK check: FAILED")

    start_angle_1_deg = DEFAULT_ANGLE_1
    start_angle_2_deg = DEFAULT_ANGLE_2
    motion_steps = 5

    angle_path = generate_angle_path(
        start_angle_1_deg=start_angle_1_deg,
        start_angle_2_deg=start_angle_2_deg,
        target_angle_1_deg=arm.current_angle_1_deg,
        target_angle_2_deg=arm.current_angle_2_deg,
        steps=motion_steps
    )

    position_path = generate_position_path(
        angle_path,
        LINK_1_LENGTH,
        LINK_2_LENGTH
    )

    animate_motion_path(position_path,
                        LINK_1_LENGTH,
                        LINK_2_LENGTH,
                        target_point
    )

if __name__ == "__main__":
    main()