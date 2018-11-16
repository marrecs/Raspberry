                                                                  #!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time

import Adafruit_CharLCD as LCD
import sys
import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

buzzer=5

GPIO.setup(buzzer, GPIO.OUT)


# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# BeagleBone Black configuration:
# lcd_rs        = 'P8_8'
# lcd_en        = 'P8_10'
# lcd_d4        = 'P8_18'
# lcd_d5        = 'P8_16'
# lcd_d6        = 'P8_14'
# lcd_d7        = 'P8_12'
# lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.message('Hello\nworld!')

# Wait 5 seconds
time.sleep(5.0)

# Demo showing the cursor.
lcd.clear()
lcd.show_cursor(True)
lcd.message('Show cursor')

time.sleep(5.0)

# Demo showing the blinking cursor.
lcd.clear()
lcd.blink(True)
lcd.message('Blink cursor')

time.sleep(5.0)

# Stop blinking and showing cursor.
lcd.show_cursor(False)
lcd.blink(False)

# Demo scrolling message right/left.
lcd.clear()
message = 'Scroll'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()

# Demo turning backlight off and on.
lcd.clear()
lcd.message('Flash backlight\nin 5 seconds...')
time.sleep(5.0)
# Turn backlight off.
lcd.set_backlight(0)
time.sleep(2.0)
# Change message.
lcd.clear()
lcd.message('Goodbye!')
# Turn backlight on.
lcd.set_backlight(1)


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
                        lcd.clear()
                        lcd.message('Has premut ' + str(MATRIX[i] [j]))
                        for temps in range(MATRIX[i] [j]):
                            GPIO.output(buzzer,GPIO.HIGH)
                            print('Beep')
                            time.sleep(0.5)
                            GPIO.output(buzzer,GPIO.LOW)
                            print('No Beep')
                            time.sleep(0.5)
                        time.sleep(0.2)

                        while(GPIO.input(ROW[i]) == 0):
                            pass


                
                GPIO.output(COL[j],1)
except KeyboardInterrupt:
        GPIO.cleanup()
