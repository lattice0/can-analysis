import serial
import getch
import time
import threading

ser = serial.Serial('/dev/ttyACM0', 115200)
known = []
f = open('trace.txt', 'w')
id_ = True
line_ = False

def write_break_line():
    while True:
        key = ord(getch.getch())
        if key==98:
            f.write("---\n")
            print("---")
        if key==113:
            exit()

#t = threading.Thread(target=write_break_line)
#t.start()
while 1:
    line = str(ser.readline())
    if not 'CAN' in line:
        try:
            a = line.split(',')
            id = a[0].replace('ID: ', '')
            data = a[1].replace('Data: ', '')
            data = data.split(' ')
        except:
            f.write("ERROR: " + str(line))
            print("ERROR: " + str(line))
        if id_:
            if not id in known:
                print(str(id) + ":" + str(data))
                known.append(id)
                f.write(str(id)+"\n")  # python will convert \n to os.linesep
        if line_:
            if not line in known:
                print(line)
                known.append(line)
                f.write(str(line)+"\n")  # python will convert \n to os.linesep
    else:
        print(line)

f.close()  # you can omit in most cases as the destructor will call it
ser.close()
