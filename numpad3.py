import sys
import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

MATRIX = [ [1,2,3,'A'],
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D']]

#ROW = [7,11,13,15]
#COL = [12,16,18,22]

ROW = [21,20,16,12] #negres
COL = [26,19,13,6] #blancs #18,23,24,25] 

print ("Pas1")

for j in range(4):
    #print [j]
    #print COL[j]

    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j],1)

    

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #print [i]
    #print ROW[i]

try:
        while(True):
            for j in range(4):
                GPIO.output(COL[j],0)
                #print [j]
                #print "pas2"
                #print (MATRIX[i] [j])

                for i in range(4):
                    #print (MATRIX[i] [j])
                    #time.sleep(0.82)

                    #print i
                    #print "pas3"
                    if GPIO.input(ROW[i]) == 0:
                        print (MATRIX[i] [j])
                        time.sleep(0.2)

                        while(GPIO.input(ROW[i]) == 0):
                            pass


                
                GPIO.output(COL[j],1)
except KeyboardInterrupt:
        GPIO.cleanup()
