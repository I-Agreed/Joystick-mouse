from Data import DataCollector
import mouse
import time

port = "COM3"

sensitivity = 1
delay = 0.01



collector = DataCollector(port)

while 1:
    data = collector.get()
    if data:
        mouse.changePos(data[0]*sensitivity, data[1]*sensitivity)
    time.sleep(delay)
