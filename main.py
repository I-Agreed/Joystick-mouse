from Data import DataCollector
import mouse
import time

port = "COM3"

sensitivity = 10
delay = 0.0



collector = DataCollector(port)

while 1:
    data = collector.get()
    if data:
        mouse.changePos(data[0]*sensitivity, data[1]*sensitivity)
    time.sleep(delay)
