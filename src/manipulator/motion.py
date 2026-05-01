def generate_angle_path(start_angle_1, start_angle_2, target_angle_1, target_angle_2, steps):
    if not isinstance(steps, int):
        raise TypeError("steps must be an integer")

    if steps <= 0:
        raise ValueError("steps must be greater than 0")

    angle_step_1 = (target_angle_1-start_angle_1) / steps
    angle_step_2 = (target_angle_2 - start_angle_2) / steps

    angles_of_motion = []

    for i in range(steps + 1):
        new_angle_1 = start_angle_1 + angle_step_1 * i
        new_angle_2 = start_angle_2 + angle_step_2 * i

        angles_of_motion.append((new_angle_1, new_angle_2))

    return angles_of_motion

if __name__ == "__main__":
    print(generate_angle_path(10, 20, 50, 100, 4))