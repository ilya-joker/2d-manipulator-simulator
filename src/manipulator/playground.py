def visualize_manipulator(first_point, second_point, link_1_length, link_2_length, target_point=None):
    x1, y1 = first_point
    x2, y2 = second_point

    plt.figure(figsize=(8, 8))

    draw_workspace(link_1_length, link_2_length)

    plt.plot([0, x1], [0, y1], "o-r", label="Link 1")
    plt.plot([x1, x2], [y1, y2], "o-b", label="Link 2")

    if target_point is not None:
        target_x, target_y = target_point
        plt.plot(target_x, target_y, "go", label="Target")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    workspace_radius = link_1_length + link_2_length
    margin = 1.0

    plt.xlim(-workspace_radius - margin, workspace_radius + margin)
    plt.ylim(-workspace_radius - margin, workspace_radius + margin)

    plt.show()