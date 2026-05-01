# def motion_links(initial_angle, target_angle, step):
#     result = []
#     for i in range(initial_angle,target_angle, step):
#         result.append((i, min(i + step,target_angle)))
#     return result



# def motion_links(initial_angle, target_angle, step):
#     x_initial, y_initial = initial_angle
#     x_target, y_target = target_angle
#
#     result_x = []
#     result_y = []
#     for i in range(x_initial,x_target, step):
#         result_x.append(i)
#
#     for i in range(y_initial,y_target, step):
#         result_y.append(i)
#
#     result = list(zip(result_x, result_y))
#     return result
#
# print(motion_links((0,0), (1,1), 10))

def motion_links(start_angle_1, start_angle_2, target_angle_1, target_angle_2, step):
