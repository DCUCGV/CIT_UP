import time
import serial

import MySQLdb
from datetime import datetime
port = serial.Serial("/dev/ttyACM0",baudrate=9600)

db = MySQLdb.connect("127.0.0.1","yuri","1234","CIT_UP")
curs = db.cursor()

id = 1
name = "Trashcan1"
date = datetime.now()
while True:
    try : 
        if port.in_waiting !=0:
            
            volume = port.readline()
            volume = (str)(volume[:-2].decode())
            
            print("id : "+str(id))
            print("name : "+name)
            print("volume : "+str(volume))
            print("date : "+str(date))
            
            
            curs.execute("""INSERT INTO info (id,name, volume, date) VALUES (%s, %s, %s, %s)""",(id, name, volume, date))
           
            db.commit()
            
            time.sleep(0.5)
            id+=1
    except KeyboardInterrupt:
        break
port.close()
db.close()

