import serial

"""

The "Login/Password: " prompts do not have an end-line

"""

ser = serial.Serial(port='COM7', baudrate=115200, timeout=2)

ser.write(b'\n')
#ser.write(b'root\n')

#ser.write(b'ps\n')

while True:
    g = ser.readline()
    print(g)
    
