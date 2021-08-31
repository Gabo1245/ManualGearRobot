import wpilib
import RobotMap
from OI import OI
from Subsystems.DriveTrain.DriveTrain import Drivetrain



class RobotContainer:

    def __init__(self):
        self.oi = OI()
        self.drivetrain = Drivetrain(self.oi)
        
        
        

        

        
    