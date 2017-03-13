import argparse
import serial
ser = serial.Serial('/dev/ttyACM0', 115200)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ids', nargs='+', help='List of IDs to follow')
args = parser.parse_args()
ids = vars(args)['ids']

print("Following ids: " + str(ids))

while 1:
    line = str(ser.readline())
    if not 'CAN' in line:
        try:
            a = line.split(',')
            id = a[0].replace('ID: ', '')
            data = a[1].replace('Data: ', '')
            data = data.split(' ')
            if id in ids:
                print(line)
            print('id not:'+id)
            print('id type:'+type(id))
            print('ids:'+str(ids))
        except:
            #f.write("ERROR: " + str(line))
            print("ERROR: " + str(line))
    else:
        print(line)
