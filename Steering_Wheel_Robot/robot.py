import wpilib
import commands2
from commands2 import CommandScheduler
from wpilib import SmartDashboard
from RobotContainer import RobotContainer
from Commands.Drive.Drive import Drive





 
class Robot(commands2.TimedCommandRobot):
    
    #This will execute when the robot starts
    def robotInit(self) -> None:
       self.robotcontainer = RobotContainer()
       
       
        
    def robotPeriodic(self):
        CommandScheduler.getInstance().run()
        
        
    
    def autonomousInit(self):
        pass
        
        
    def autonomousPeriodic(self):
        pass

    def teleopInit(self): 
        pass

    def teleopPeriodic(self):
        CommandScheduler.getInstance().run()
        self.robotcontainer.drivetrain.setDefaultCommand(Drive(self.robotcontainer.drivetrain, self.robotcontainer.oi))

if __name__ == "__main__":
    wpilib.run(Robot)
    