import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from manipulator.math_utils import calculate_workspace_bounds


def draw_workspace(link_1_length, link_2_length):
    outer_radius, inner_radius = calculate_workspace_bounds(link_1_length, link_2_length)
    outer_circle = plt.Circle(
        (0, 0),
        outer_radius,
        fill=False,
        linestyle="--",
        label="Max reach"
    )

    plt.gca().add_patch(outer_circle)

    if inner_radius > 0:
        inner_circle = plt.Circle(
            (0, 0),
            inner_radius,
            fill=False,
            linestyle=":",
            label="Min reach"
        )

        plt.gca().add_patch(inner_circle)

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

    workspace_radius = link_1_length + link_2_length
    margin = 1.0

    plt.xlim(-workspace_radius - margin, workspace_radius + margin)
    plt.ylim(-workspace_radius - margin, workspace_radius + margin)

    # Get current coordinate axes and keep equal scale on X and Y.
    # This prevents workspace circles from looking like ellipses.
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")

    plt.legend()
    plt.title("2-Link Manipulator")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def visualize_motion_path(position_path, link_1_length, link_2_length, target_point=None):
    plt.figure(figsize=(8, 8))
    draw_workspace(link_1_length, link_2_length)
    if target_point is not None:
        target_x, target_y = target_point
        plt.plot(target_x, target_y, "go", label="Target")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)

    workspace_radius = link_1_length + link_2_length
    margin = 1.0

    plt.xlim(-workspace_radius - margin, workspace_radius + margin)
    plt.ylim(-workspace_radius - margin, workspace_radius + margin)

    # Get current coordinate axes and keep equal scale on X and Y.
    # This prevents workspace circles from looking like ellipses.
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")

    # Draw every manipulator position from the generated motion path.
    # Each item in position_path contains two points:
    # first link endpoint and second link endpoint.
    for step_index, ((x1, y1), (x2, y2)) in enumerate(position_path):
        if step_index == 0:
            plt.plot([0, x1], [0, y1], "o-r", label="Link 1")
            plt.plot([x1, x2], [y1, y2], "o-b", label="Link 2")
        else:
            plt.plot([0, x1], [0, y1], "o-r")
            plt.plot([x1, x2], [y1, y2], "o-b")

    plt.legend()
    plt.title("2-Link Manipulator Motion Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def animate_motion_path(position_path, link_1_length, link_2_length, target_point=None):

    # Draw every manipulator position from the generated motion path.
    # Each item in position_path contains two points:
    # first link endpoint and second link endpoint.
    plt.figure(figsize=(8, 8))
    for step_index, ((x1, y1), (x2, y2)) in enumerate(position_path):
        plt.cla()


        draw_workspace(link_1_length, link_2_length)
        if target_point is not None:
            target_x, target_y = target_point
            plt.plot(target_x, target_y, "go", label="Target")

        plt.axhline(0)
        plt.axvline(0)
        plt.grid(True)

        workspace_radius = link_1_length + link_2_length
        margin = 1.0

        plt.xlim(-workspace_radius - margin, workspace_radius + margin)
        plt.ylim(-workspace_radius - margin, workspace_radius + margin)

        # Get current coordinate axes and keep equal scale on X and Y.
        # This prevents workspace circles from looking like ellipses.
        ax = plt.gca()
        ax.set_aspect("equal", adjustable="box")


        plt.plot([0, x1], [0, y1], "o-r", label="Link 1")
        plt.plot([x1, x2], [y1, y2], "o-b", label="Link 2")


        plt.legend()
        plt.title("2-Link Manipulator Motion Path")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.pause(0.3)

    plt.show()

def animate_motion_path_func(position_path, link_1_length, link_2_length, target_point=None):
    fig, ax = plt.subplots(figsize=(8, 8))

    def update(frame):
        ax.cla()
        # здесь видны position_path, link_1_length и т.д.
        # frame — номер кадра, используй его чтобы взять нужное положение из position_path

        x1, y1 = position_path[frame][0]  # → (1, 0) — first_point
        x2, y2 =position_path[frame][1]  # → (2, 0) — second_point

        draw_workspace(link_1_length, link_2_length)
        if target_point is not None:
            target_x, target_y = target_point
            plt.plot(target_x, target_y, "go", label="Target")

        plt.axhline(0)
        plt.axvline(0)
        plt.grid(True)

        workspace_radius = link_1_length + link_2_length
        margin = 1.0

        plt.xlim(-workspace_radius - margin, workspace_radius + margin)
        plt.ylim(-workspace_radius - margin, workspace_radius + margin)

        # Get current coordinate axes and keep equal scale on X and Y.
        # This prevents workspace circles from looking like ellipses.
        ax.set_aspect("equal", adjustable="box")

        plt.plot([0, x1], [0, y1], "o-r", label="Link 1")
        plt.plot([x1, x2], [y1, y2], "o-b", label="Link 2")

        plt.legend()
        plt.title("2-Link Manipulator Motion Path")
        plt.xlabel("X")
        plt.ylabel("Y")


    ani = FuncAnimation(fig, update, frames=len(position_path), interval=100)
    plt.show()
