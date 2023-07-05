from robot_control_class import RobotControl
RobotControl = RobotControl()
a = RobotControl.get_laser(360)
# is there a wall less than 1 meter from the robot?
# if yes, stop the robot moving 
# if no, keep moving
while a > 1:
    print(a)
    RobotControl.move_straight()
    a = RobotControl.get_laser(360)
#stop the robot
RobotControl.stop_robot()
print("Robot stopped " +str(a) +' meters away from the wall.')