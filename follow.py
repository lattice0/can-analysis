import argparse
import serial
ser = serial.Serial('/dev/ttyACM0', 115200)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ids', nargs='+', help='List of IDs to follow')
args = parser.parse_args()
ids = vars(args)['ids']

memory = {}
print("Following ids: " + str(ids))
for i in ids:
    memory[i] = ""
print(memory)
while True:
    line = str(ser.readline())
    if not 'CAN' in line:
        try:
            a = line.split(',')
            id = a[0].split(' ')[1]
            #data = a[1].replace('Data: ', '')
            #data = data.split(' ')
            if id in ids:
                if not line in memory[id]:
                    memory[id] = line
                    print(line)
                else:
                    pass
            else:
                #print('id not:'+id)
                #print('id type:'+str(type(id)))
                #print('ids:'+str(ids))
                pass
        except Exception as e:
            #f.write("ERROR: " + str(line))
            print("ERROR: " + str(line) + " error: " +str(e))
            pass
    else:
        print(line)
