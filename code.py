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

button_stat = False
count = 0

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
            time.sleep(1)
            player_seq.append(1)
            blink((0, 0, 0), 6, 5)
            np.show()
        time.sleep(.05)
    if value == touch2:
        if value.value == True:
            blink((1, 255, 1), 9, 8)
            np.show()
            time.sleep(1)
            player_seq.append(2)
            blink((0, 0, 0), 9, 8)
            np.show()
        time.sleep(.05)
    if value == touch6:
        if value.value == True:
            blink((1, 1, 255), 3, 4)
            np.show()
            time.sleep(1)
            player_seq.append(3)
            blink((0, 0, 0), 3, 4)
            np.show()
        time.sleep(.05)
    if value == touch5:
        if value.value == True:
            blink((255, 255, 0), 0, 1)
            np.show()
            time.sleep(1)
            player_seq.append(4)
            blink((0, 0, 0), 0, 1)
            np.show()
        time.sleep(.05)

def comp_game():
    rand = random.randint(0, 3)
    game_seq.append(rand)
    
def check(game, player):
    for thing in game:
        if thing == player[1]:
            print("working")
    
while True:
    if button_a.value:
        button_stat = not button_stat
        time.sleep(.5)
        player_seq = []
    if button_stat:
        comp_game()
        lights(touch1)
        lights(touch2)
        lights(touch5)
        lights(touch6)

