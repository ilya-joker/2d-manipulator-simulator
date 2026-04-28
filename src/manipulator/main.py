from config import LINK_1_LENGTH, LINK_2_LENGTH, DEFAULT_ANGLE_1, DEFAULT_ANGLE_2
from manipulator.visualizer import visualize_manipulator
from forward_kinematics import first_link_end, second_link_end
from printer import print_manipulator_state


def main():
    first_point = first_link_end(LINK_1_LENGTH, DEFAULT_ANGLE_1)
    second_point = second_link_end(
        LINK_1_LENGTH,
        LINK_2_LENGTH,
        DEFAULT_ANGLE_1,
        DEFAULT_ANGLE_2
    )

    print_manipulator_state(
        LINK_1_LENGTH,
        LINK_2_LENGTH,
        DEFAULT_ANGLE_1,
        DEFAULT_ANGLE_2,
        first_point,
        second_point
    )

    visualize_manipulator(first_point,second_point)


if __name__ == "__main__":
    main()