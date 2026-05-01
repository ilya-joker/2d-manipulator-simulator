from manipulator.motion import generate_angle_path


def main():
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


if __name__ == "__main__":
    main()