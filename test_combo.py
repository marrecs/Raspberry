import time
import Adafruit_CharLCD as LCD
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

control_pins = [4,27,10,9]

# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.message('Hello\nworld!')
# Wait 5 seconds
time.sleep(2.0)
lcd.clear()



for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
for i in range(512*90/360):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      lcd.clear()
      lcd.message('Pin:%d Ha:%d I:%d'  % (pin, halfstep,i))
      time.sleep(0.0101)
GPIO.cleanup()
