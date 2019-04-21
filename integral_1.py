import serial
#from firebase import firebase
import time
import requests
import json
import datetime

#firebase = firebase.FirebaseApplication('https://bmss-6ef1b.firebaseio.com', None)
ser = serial.Serial('/dev/ttyACM0',9600)
n=0
current_array = []
int_current = []
integrate_current = 0
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
    current_array.append(Current)
    if n>=2:
        int_current.append(2.5*(current_array[n-2]+current_array[n-1]))
        integrate_current = 2.5*(current_array[n-2]+current_array[n-1])
    n =n+1
    print current_array
    print "***********************"
    print integrate_current
    print "***********************"
    data = {'time' : int(time.time()), 'Temp' : Temp, 'Current' : Current, 'Voltage' : Voltage}
    #post = requests.post('https://bmss-6ef1b.firebaseio.com' +'/'+ 'data.json', data= json.dumps(data))
    file = open("test1.txt", "a")
    file.write(str(time.ctime())+"\t"+str(Temp)+"\t"+str(Current)+"\t"+str(Voltage)+"\t"+str(integrate_current)+"\n")
    file.close()
