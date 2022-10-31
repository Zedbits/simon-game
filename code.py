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

game_seq = []
button_stat = False

game_stat = False

"""
Function: blink
Description: this function blinks a color
Parameters: color(tuple) - the rgb value of the blinking color
Return: none
"""
def blink(color, number1, number2):
    np[number1] = color
    np[number2] = color
    
def reset():
    global game_stat, player_val, game_seq
    np.fill((255, 0, 0))
    time.sleep(1)
    np.fill((0, 0, 0))
    time.sleep(1)
    player_val = -1
    game_seq = []
    game_stat = False
    print('Game reset')
    
def lights():
    player_val = -1
    index = 0
    for index in range(len(game_seq)):
        while not touch1.value and not touch2.value and not touch5.value and not touch6.value:
            pass
            
        if touch1.value:
            blink((255, 1, 1), 6, 5)
            np.show()
            time.sleep(1)
            player_val = 1
            player_touch = True
            blink((0, 0, 0), 6, 5)
            np.show()
        time.sleep(.05)
        if touch2.value:
            blink((1, 255, 1), 9, 8)
            np.show()
            time.sleep(1)
            player_val = 0
            player_touch = True
            blink((0, 0, 0), 9, 8)
            np.show()
        time.sleep(.05)
        if touch6.value:
            blink((1, 1, 255), 3, 4)
            np.show()
            time.sleep(1)
            player_val = 2
            player_touch = True
            blink((0, 0, 0), 3, 4)
            np.show()
        time.sleep(.05)
        if touch5.value:
            blink((255, 255, 0), 0, 1)
            np.show()
            time.sleep(1)
            player_val = 3
            player_touch = True
            blink((0, 0, 0), 0, 1)
            np.show()
        if game_seq[index] == player_val:
            index += 1
            np.fill((0, 255, 0))
            time.sleep(.5)
            np.fill((0, 0, 0))
            print(index)
        else:
            reset()
            print('Breaking')
            break
    time.sleep(.05)

def comp():
    rand = random.randint(0, 3)
    game_seq.append(rand)
    for item in game_seq:
        if item == 0:
            blink((1, 255, 1), 9, 8)
            np.show()
            time.sleep(1)
            blink((0, 0, 0), 9, 8)
            np.show()
            time.sleep(1)
        if item == 1:
            blink((255, 1, 1), 6, 5)
            np.show()
            time.sleep(1)
            blink((0, 0, 0), 6, 5)
            np.show()
            time.sleep(1)
        if item == 2:
            blink((1, 1, 255), 3, 4)
            np.show()
            time.sleep(1)
            blink((0, 0, 0), 3, 4)
            np.show()
            time.sleep(1)
        if item == 3:
            blink((255, 255, 0), 0, 1)
            np.show()
            time.sleep(1)
            blink((0, 0, 0), 0, 1)
            np.show()
            time.sleep(1)

def player():
    lights()


while True:
    print("main loop",game_stat)
    time.sleep(0.05)
    if not game_stat:
        if button_a.value:
            button_stat = not button_stat
            time.sleep(.5)
            game_stat = True
    else:
        comp()
        player()
        print(game_stat)
        print(game_seq)

