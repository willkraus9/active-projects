## Unit 1: Intro to Course
- Python = most popular language w/ C++ (Python = best for research)
- AI libraries for robotics = Python
- easiest way to learn ROS = Python
* run in terminal: python (name of file.py)
## Unit 2: Python Essentials
- RobotControl = Python class for managing ROS stuff
- course uses ROS Noetic (comes with Python 3)
- Import = include another program in code from module [from <name of module> import <method / class to use>]
- create variables: var_name = what it does
- a = rc.get_laser(360)
- variable name = method(parameter)
- in this case, 360 corresponds to the middle laser on the robot (720 beams in total)
- Variables = no need to declare type (already done)
## Unit 4: Methods
- Method = group set of statements to be used >1 in program
- def (name of method) (): [stuff inside method]
- calling: (name of method)(parameters)
- Parameters = variables to be used inside method
-  Return: added inside parameter to return object 
## Unit 5: OOP 
- kind of like procedural (with methods), but different
- Wraps data / functions inside objects (aka classes)
- easier to understand, upgrade, maintain, etc. 
- Defined by two things: 
1. Attributes (data associated with objects)
2. Procedures or methods associated with objects
- Python Class = code template creating object
- my_object = Jedi("Qui-Jong-Jin") [object has variable of type Jedi]
- class Jedi:
    def __init__(self, name): #method 1: class constructor = __init__
        self.jedi_name = name
          #initial call for object
    def say_hi(self): #method 2 
        #self keyword = method belongs to the class
        print('Hello, my name is ', self.jedi_name)
- j1 = Jedi('ObiWan')
- j1.say_hi()
