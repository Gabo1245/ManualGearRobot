from wpilib import Joystick
import RobotMap

class OI():

    def __init__(self):
        super().__init__()
        self.stick = Joystick(RobotMap.CONTROLLER)
        