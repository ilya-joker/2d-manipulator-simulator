import math
from manipulator.forward_kinematics import first_link_end, second_link_end
from manipulator.inverse_kinematics import find_angles
from manipulator.math_utils import distance

link_1_length = 1
link_2_length = 1

def test_target(x, y, elbow):
    angles = find_angles(x, y, link_1_length, link_2_length, elbow=elbow)

    if angles is None:
        return False

    angle_1_rad, angle_2_rad = angles

    angle_1_link = math.degrees(angle_1_rad)
    angle_2_link = math.degrees(angle_2_rad)

    second_point = second_link_end(
        link_1_length,
        link_2_length,
        angle_1_link,
        angle_2_link
    )

    target_point = (x, y)
    error = distance(target_point, second_point)

    return error < 1e-6

def test_elbow_modes_have_different_joint_positions():
    x, y = 1, 1

    down_angles = find_angles(
        x,
        y,
        link_1_length,
        link_2_length,
        elbow="down"
    )

    up_angles = find_angles(
        x,
        y,
        link_1_length,
        link_2_length,
        elbow="up"
    )

    if down_angles is None or up_angles is None:
        return False

    down_angle_1_rad, down_angle_2_rad = down_angles
    up_angle_1_rad, up_angle_2_rad = up_angles

    down_angle_1_deg = math.degrees(down_angle_1_rad)
    up_angle_1_deg = math.degrees(up_angle_1_rad)

    down_first_point = first_link_end(link_1_length, down_angle_1_deg)
    up_first_point = first_link_end(link_1_length, up_angle_1_deg)

    elbow_distance = distance(down_first_point, up_first_point)

    return elbow_distance > 1e-6  # True means elbows are in different positions

def main():
    test_targets = [
        (2, 0),
        (1, 1),
        (1, 1),
        (3, 0),
    ]

    test_elbows = [
        "down",
        "up",
        "down",
        "up"
    ]
    expected_results = [
        True,
        True,
        True,
        False,
    ]

    test_cases = list(zip(test_targets, test_elbows, expected_results))

    for target, elbow, expected in test_cases:
        x, y = target
        actual = test_target(x, y, elbow)
        test_passed = actual == expected
        test_result_text = "PASSED" if test_passed else "FAILED"

        print(
            f"Target: {target} | "
            f"elbow: {elbow} | "
            f"expected: {expected} | "
            f"actual: {actual} | "
            f"result: {test_result_text}"
        )
    elbow_modes_different = test_elbow_modes_have_different_joint_positions()
    elbow_test_result = "PASSED" if elbow_modes_different else "FAILED"

    print()
    print(f"Elbow modes are different | result: {elbow_test_result}")

if __name__ == "__main__":
    main()