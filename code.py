import board
import digitalio as dio
import time
import neopixel
import random
import touchio


button_a = dio.DigitalInOut(board.BUTTON_A)
button_a.direction = dio.Direction.INPUT
button_a.pull = dio.Pull.DOWN
touch_pad1 = board.A1
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A2
touch2 = touchio.TouchIn(touch_pad2)
touch_pad5 = board.A5
touch5 = touchio.TouchIn(touch_pad5)
touch_pad6 = board.A6
touch6 = touchio.TouchIn(touch_pad6)

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=.1, auto_write=False)

win = True
game_seq = []
player_seq = []
rand = random.randint(0, 3)
button_stat = False

"""
Function: blink
Description: this function blinks a color
Parameters: color(tuple) - the rgb value of the blinking color
Return: none
"""
def blink(color, number1, number2):
    np[number1] = color
    np[number2] = color

def lights(value):
    if value == touch1:
        if value.value == True:
            blink((255, 1, 1), 6, 5)
            np.show()
        else:
            blink((0, 0, 0), 6, 5)
            np.show()
        time.sleep(.05)
    if value == touch2:
        if value.value == True:
            blink((1, 255, 1), 9, 8)
            np.show()
        else:
            blink((0, 0, 0), 9, 8)
            np.show()
        time.sleep(.05)
    if value == touch6:
        if value.value == True:
            blink((1, 1, 255), 3, 4)
            np.show()
        else:
            blink((0, 0, 0), 3, 4)
            np.show()
        time.sleep(.05)
    if value == touch5:
        if value.value == True:
            blink((255, 255, 0), 0, 1)
            np.show()
        else:
            blink((0, 0, 0), 0, 1)
            np.show()
        time.sleep(.05)
while True:
    if button_a.value:
        button_stat = not button_stat
        time.sleep(1)
    print(button_stat)
    if button_stat:
        lights(touch1)
        lights(touch2)
        lights(touch5)
        lights(touch6)
    
