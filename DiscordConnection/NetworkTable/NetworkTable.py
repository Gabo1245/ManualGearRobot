import threading
from networktables import NetworkTables 

class NetworkTableConnection():

    def __init__(self, serv):
        
        self.cond = threading.Condition()
        self.notified = [False]
        
        NetworkTables.initialize(server=serv)
        NetworkTables.addConnectionListener(self.connectionListener, immediateNotify=True)
        
        

    def connectionListener(self, connected, info):
        print(info, '; Connected=%s' % connected)
        with self.cond:
            self.notified[0] = True
            self.cond.notify()
        
        with self.cond:
            print("Waiting")
            if not self.notified[0]:
                self.cond.wait()
        print("Connected!")

    
    def getTableValue(self, NetworkTable, valuename):
    
        self.table = NetworkTables.getTable(NetworkTable)
        self.value = self.table.getNumber(valuename, -1.0)
        
       
        return self.value



    