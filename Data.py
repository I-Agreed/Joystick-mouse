import serial

class DataCollector:
    def __init__(self, port):
        self.port = port
        self.serial = serial.Serial(self.port, 9600)
    
    def get(self):
        data = self.serial.read().split("|")[-1]
        data = eval(data)
        return data