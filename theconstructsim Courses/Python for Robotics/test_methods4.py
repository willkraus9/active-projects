from robot_control_class import RobotControl
robotcontrol = RobotControl(robot_name="summit")

robotcontrol.move_straight_time("forward", 0.3, 5)
robotcontrol.turn("counter-clockwise", 0.3, 7)
robotcontrol.move_straight_time("forward", 0.3, 5)
robotcontrol.turn("counter-clockwise", 0.3, 7)
robotcontrol.move_straight_time("forward", 0.3, 5)

