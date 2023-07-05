from robot_control_class import RobotControl
# is there a wall less than 1 meter from the robot?
# if no, keep moving and print reading
# if yes, stop and print reading

RobotControl = RobotControl()
a = RobotControl.get_laser(360)
if a < 1:
    print(a)
    #Stop the robot
    RobotControl.stop_robot()
else:
    print(a)
    #keep moving
    RobotControl.move_straight()