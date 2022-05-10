
class myPacket:
    def __init__(self, name, index, BDADDR, EVTtype, time, length, direction):
        self.name = name
        self.index = index
        self.BDADDR = BDADDR
        self.EVTtype = EVTtype
        self.time = time
        self.length = length
        self.direction = direction
        
    def getName(self):
        return self.name
    
    def getIndex(self):
        return self.index
    
    def getBDADDR(self):
        return self.BDADDR
    
    def getEVTtype(self):
        return self.EVTtype
    
    def getTime(self):
        return self.time
    
    def getLength(self):
        return self.length
    
    def getDirection(self):
        return self.direction