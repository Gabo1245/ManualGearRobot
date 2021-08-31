import wpilib
from commands2 import SubsystemBase
from ctre import TalonSRX, ControlMode
from wpilib import Talon
from OI import OI
import RobotMap




class Drivetrain(SubsystemBase):
    def __init__(self, oi: OI):
        super().__init__()
        self.oi = oi
        self.LEFTTALON1 = Talon(RobotMap.LEFTTALONS[0])
        self.LEFTTALON2 = Talon(RobotMap.LEFTTALONS[1])
        self.RIGHTTALON1 = Talon(RobotMap.RIGHTTALONS[0])
        self.RIGHTTALON2 = Talon(RobotMap.RIGHTTALONS[1])
        self.shift = 0
    
    def changeShift(self, leftshift, rightshift):
        if (self.shift <= 5 and self.shift > 0 and self.oi.stick.getRawButtonReleased(leftshift)):
            self.shift -= 1
            
        if (self.shift >= 0 and self.shift < 5 and self.oi.stick.getRawButtonReleased(rightshift)):
            self.shift += 1
        wpilib.SmartDashboard.putNumber("Shift", float(self.shift))
        
    
    def setMotors(self, leftspeed, rightspeed):
        velocity = float(self.shift/5)
        self.LEFTTALON1.set(velocity*(-leftspeed-rightspeed))
        self.LEFTTALON2.set(velocity*(-leftspeed-rightspeed))
        self.RIGHTTALON1.set(velocity*(leftspeed-rightspeed))
        self.RIGHTTALON2.set(velocity*(leftspeed-rightspeed))
        print(self.shift)
    
        
    

