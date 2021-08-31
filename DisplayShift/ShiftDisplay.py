import sys, pygame
import time as tim
import networktables
from NetworkTable.NetworkTable import NetworkTableConnection

class ShiftDisplay():
    def __init__(self):
        self.networktableconnection = NetworkTableConnection("127.0.0.1")
        
        
        pygame.init()
        self.white = (255, 255, 255)
        self.size = 800, 540
        self.black = (0, 0, 0)

        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font('DisplayShift/Formula1-Bold.ttf', 200)
        self.textrect = (300,150)

    def Display(self):
        time = tim.time()
        self.shiftnum = self.networktableconnection.getTableValue('SmartDashboard', 'Shift')
        while 1:
            for event in pygame.event.get():
                if int(tim.time() - time) % 0.5 == 0:
                    self.shiftnum = int(self.networktableconnection.getTableValue('SmartDashboard', 'Shift'))
                self.text = self.font.render(str(self.shiftnum), True, self.white)
                self.screen.fill(self.black)
                self.screen.blit(self.text, self.textrect)
                pygame.display.flip()
                if event.type == pygame.QUIT: sys.exit()
    

