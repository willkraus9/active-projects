import time
from robot_control_class import RobotControl

RobotControl = RobotControl(robot_name="summit") 

def moving_time():
    number = int(input('Straight run time: '))
    RobotControl.move_straight()
    time.sleep(number)
    RobotControl.stop_robot()

moving_time()