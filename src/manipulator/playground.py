from manipulator.visualizer import draw_workspace, animate_motion_path_func

position_path = [
    ((1, 0), (2, 0)),
    ((0, 1), (0, 2)),
]
target_point = (0, 2)
animate_motion_path_func(position_path, link_1_length=1, link_2_length=1, target_point=target_point)