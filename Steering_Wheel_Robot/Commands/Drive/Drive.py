import wpilib
from commands2 import CommandBase
from Subsystems.DriveTrain.DriveTrain import Drivetrain
from OI import OI
import RobotMap

class Drive(CommandBase):

    def __init__(self, drivetrain: Drivetrain, oi: OI):
        super().__init__()
        self.drivetrain = drivetrain
        self.oi = oi
        self.addRequirements([drivetrain])
        

    def initialize(self):
        pass
    
    def execute(self):
        self.drivetrain.changeShift(RobotMap.DOWNSHIFT, RobotMap.UPSHIFT)
        self.drivetrain.setMotors(self.oi.stick.getRawAxis(RobotMap.AXIS[0]), 
        self.oi.stick.getRawAxis(RobotMap.AXIS[1]))