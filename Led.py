import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

GPIO.setup(6,GPIO.OUT)
print "LED on"
GPIO.output(6,GPIO.HIGH)
time.sleep(10)
print "LED off"
GPIO.output(6,GPIO.LOW)

GPIO.cleanup()
