import serial

class DataCollector:
    def __init__(self, port):
        self.port = port
        self.serial = serial.Serial(self.port, 9600)
    
    def get(self):
        rawData = self.serial.readline().decode("utf-8", "ignore")
        try:
            data = eval(rawData)
        except ValueError:
            return None
        print(data)
        
        return data