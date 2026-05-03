from manipulator.math_utils import distance
from manipulator.motion import generate_angle_path, generate_position_path


def test_generate_angle_path():
    actual = generate_angle_path(10, 20, 50, 100, 4)

    expected = [
        (10.0, 20.0),
        (20.0, 40.0),
        (30.0, 60.0),
        (40.0, 80.0),
        (50.0, 100.0),
    ]

    result = actual == expected
    result_text = "PASSED" if result else "FAILED"

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print(f"Result:   {result_text}")

def test_generate_position_path():
    """
        Check that generate_position_path correctly converts an angle path
        into a list of manipulator positions.

        Each item in angle_path contains two angles in degrees:
        (angle_1_deg, angle_2_deg).

        For each pair of angles, generate_position_path should calculate:
        - first_point: endpoint of the first link;
        - second_point: endpoint of the second link / end effector.

        The test uses simple known cases:
        - angles (0, 0) should place the manipulator horizontally:
          first_point = (1, 0), second_point = (2, 0)
        - angles (90, 0) should place both links vertically:
          first_point = (0, 1), second_point = (0, 2)

        Coordinates are compared using distance instead of direct equality,
        because trigonometric calculations can produce tiny floating-point errors
        such as 6.123e-17 instead of 0.
        """

    link_length1 = 1
    link_length2 = 1

    angle_path = [
        (0, 0),
        (90, 0),
    ]

    expected  = [
        ((1, 0), (2, 0)),
        ((0, 1), (0, 2)),
    ]

    actual = generate_position_path(angle_path, link_length1, link_length2)

    # Compare actual and expected positions for each step of the motion path.
    for step_index, (actual_position, expected_position) in enumerate(zip(actual, expected)):
        actual_first_point, actual_second_point = actual_position
        expected_first_point, expected_second_point = expected_position

        # Use distance instead of == because trigonometric calculations have small floating-point errors.
        first_error = distance(actual_first_point, expected_first_point)
        second_error = distance(actual_second_point, expected_second_point)

        test_passed = first_error < 1e-6 and second_error < 1e-6
        result_text = "PASSED" if test_passed else "FAILED"

        print(
            f"Step: {step_index} | "
            f"first error: {first_error} | "
            f"second error: {second_error} | "
            f"result: {result_text}")



def main():
    test_generate_angle_path()
    test_generate_position_path()



if __name__ == "__main__":
    main()
