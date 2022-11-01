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
def flash_green():
    for i in range(2):
            np.fill((0, 255, 0))
            np.show()
            time.sleep(.05)
            np.fill((0, 0, 0))
            np.show()
            time.sleep(.05)
def flash_red():
    for i in range(2):
        np.fill((255, 0, 0))
        np.show()
        time.sleep(.05)
        np.fill((0, 0, 0))
        np.show()
        time.sleep(.05)
def show_pixel(color, pos1, pos2, thing):
    blink(color, pos1, pos2)
    np.show()
    time.sleep(thing)
    blink((0, 0, 0), pos1, pos2)
    np.show()
    time.sleep(thing)
    
def reset():
    global game_stat, player_val, game_seq
    flash_red()
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
            show_pixel((255, 0, 0), 6, 5, .5)
            player_val = 1
            print(player_val)
        time.sleep(.10)
        if touch2.value:
            show_pixel((0, 255, 0), 9, 8, .5)
            player_val = 0
            print(player_val)
        time.sleep(.10)
        if touch6.value:
            show_pixel((0, 0, 255), 3, 4, .5)
            player_val = 2
            print(player_val)
        time.sleep(.10)
        if touch5.value:
            show_pixel((255, 255, 0), 0, 1, .5)
            player_val = 3
            print(player_val)
        time.sleep(.10)
        if game_seq[index] == player_val:
            index += 1
            print(index)
        else:
            reset()
            print('Breaking')
            break
    time.sleep(.05)

def comp():
    rand = random.randint(0, 3)
    game_seq.append(rand)
    flash_green()
    for item in game_seq:
        if item == 0:
            show_pixel((1, 255, 1), 9, 8, 1)
        if item == 1:
            show_pixel((255, 1, 1), 6, 5, 1)
        if item == 2:
            show_pixel((1, 1, 255), 3, 4, 1)
        if item == 3:
            show_pixel((255, 255, 0), 0, 1, 1)

def player():
    lights()


while True:
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

