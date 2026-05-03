from manipulator.robot import TwoLinkManipulator

arm = TwoLinkManipulator(1, 1)
print(arm.get_position())
result = arm.move_to((1, 1), elbow="up")
print(result)
print(arm.get_position())