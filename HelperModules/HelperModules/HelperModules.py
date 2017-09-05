
import os
import datetime
import time

def Log(logEntry,logfilePath,maxLogSizeInBytes):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #logfilePath = "C:\\temp\\debug.log"
    #logEntry = "TEST"
    if os.path.isfile(logfilePath): 
       if os.path.getsize(logfilePath) > maxLogSizeInBytes * 1024:
          os.remove(logfilePath)

    file = open(logfilePath,'a')
    file.write(timestamp + ' - ' + logEntry + "\n")    
    file.close()


