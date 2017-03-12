import serial
import getch
import time
import threading

ser = serial.Serial('/dev/ttyACM0', 115200)
known = []
f = open('trace.txt', 'w')

def write_break_line():
    while True:
        key = ord(getch.getch())
        if key==98:
            f.write("---\n")
            print("---")
        if key==113:
            exit()

t = threading.Thread(target=write_break_line)
t.start()
while 1:
    line = str(ser.readline())
    if not 'CAN' in line:
        a = line.split(',')
        id = a[0].replace('ID: ', '')
        data = a[1].replace('Data: ', '')
        data = data.split(' ')
        if id not in known:
            print(id + ":" + data)
            known.append(id)
            f.write(id+"\n")  # python will convert \n to os.linesep
    else:
        line

f.close()  # you can omit in most cases as the destructor will call it
ser.close()
