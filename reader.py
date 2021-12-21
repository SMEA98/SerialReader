import serial 

ser = serial.Serial(
        port = 'COM17',\
        baudrate = 115200,\
        parity = serial.PARITY_NONE,\
        stopbits = serial.STOPBITS_ONE,\
        bytesize = serial.EIGHTBITS,\
        timeout =0)

print("Connected to: " + ser.portstr)
count = 1

while True:
    line = ser.readline()
    print(str(count) + str(': ') + str(line) )
    count += 1

ser.close()


