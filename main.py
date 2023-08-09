from gpio import *
from time import *

def handleSensorData():
	value = digitalRead(0)
	if value == 0:
		customWrite(1, '0')
		print("No Fire Is Detected")
	else:
		customWrite(1, '1')
		print("Fire Is Detected")
	
	
def main():
	add_event_detect(0, handleSensorData) 
	
	while True:
		delay(1000)

if __name__ == "__main__":
	main()
	
