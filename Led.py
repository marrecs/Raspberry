#16-11-2018
#Encendre un Led

#Importem llibreries
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#Definim numero de Pin
GPIO.setup(6,GPIO.OUT)


#Encenem Led
print "LED on"
GPIO.output(6,GPIO.HIGH)

#Esperem
time.sleep(10)

#Apaguem Led
print "LED off"
GPIO.output(6,GPIO.LOW)

GPIO.cleanup()
