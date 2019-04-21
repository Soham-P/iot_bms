import serial
#from firebase import firebase
import time
import requests
import json
import datetime

#firebase = firebase.FirebaseApplication('https://bmss-6ef1b.firebaseio.com', None)
ser = serial.Serial('/dev/ttyACM0',9600)
while 1:
    Temp = float(ser.readline())
    #time.sleep(1)
    Current = float(ser.readline())
    #time.sleep(1)
    Voltage = float(ser.readline())
    #time.sleep(1)
    print Temp
    print Current
    print Voltage
##    data = {'time' : int(time.time()), 'Temp' : Temp, 'Current' : Current, 'Voltage' : Voltage}
##    #post = requests.post('https://bmss-6ef1b.firebaseio.com' +'/'+ 'data.json', data= json.dumps(data))
##    file = open("test.txt", "a")
##    file.write(str(time.ctime())+"\t"+str(Temp)+"\t"+str(Current)+"\t"+str(Voltage)+"\n")
##    file.close()
