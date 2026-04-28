import math
from manipulator.forward_kinematics import first_link_end, second_link_end
from manipulator.inverse_kinematics import find_angles
from manipulator.math_utils import distance

link_1_length = 1
link_2_length = 1

def test_target(x, y):
    angles = find_angles(x, y, link_1_length, link_2_length)

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


def main():
    test_targets = [
        (2, 0),
        (1, 1),
        (3, 0),
    ]

    expected_results = [
        True,
        True,
        False,
    ]

    test_cases = list(zip(test_targets, expected_results))

    for target, expected in test_cases:
        x, y = target
        actual = test_target(x, y)
        test_passed = actual == expected
        test_result_text = "PASSED" if test_passed else "FAILED"

        print(
            f"Target: {target} | "
            f"expected: {expected} | "
            f"actual: {actual} | "
            f"result: {test_result_text}"
        )


if __name__ == "__main__":
    main()