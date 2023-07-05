from robot_control_class import RobotControl
RobotControl = RobotControl(robot_name="summit") 
def obtain_laser_ints():
    laser_lists = []
    for i in range(0,3):
        digit = int(input('0-719: Value ' +str(i+1) +': '))
        laser_value = float(RobotControl.get_laser_summit(digit))
        laser_lists.append([laser_value])
    print(laser_lists)
obtain_laser_ints()