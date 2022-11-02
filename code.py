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

"""
Function: flash_green
Description: This function flashes the color green on every neo pixel on the board.
Parameters: None
Return: None
"""
def flash_green():
    for i in range(2):
            np.fill((0, 255, 0))
            np.show()
            time.sleep(.05)
            np.fill((0, 0, 0))
            np.show()
            time.sleep(.05)

"""
Function: flash_red
Description: This function flashes the color red on every neo pixel on the board.
Parameters: None
Return: None
"""
def flash_red():
    for i in range(2):
        np.fill((255, 0, 0))
        np.show()
        time.sleep(.05)
        np.fill((0, 0, 0))
        np.show()
        time.sleep(.05)

"""
Function: show_pixel
Description: Main code to light up a specific neo pixel a certain color.
Parameters: color(tuple) - a tuple RGB value that will be used to light up the neo pixels a certain color.
pos1(int) - an int value that is used to light up the neo pixel at one of the two places on the playground express.
pos2(int) - another int value that will be used to light up the neo pixel at the other position.
num(floating point) - floating point value that will set how long the lights will show up for.
Return: None
"""
def show_pixel(color, pos1, pos2, num):
    blink(color, pos1, pos2)
    np.show()
    time.sleep(num)
    blink((0, 0, 0), pos1, pos2)
    np.show()
    time.sleep(num)

"""
Function: reset
Description: This function flashes red to indicate a wrong input/fail game and resets all variables back to default values.
Parameters: none
Return: None
"""
def reset():
    global game_stat, player_val, game_seq
    flash_red()
    player_val = -1
    game_seq = []
    game_stat = False

"""
Function: lights
Description: This function is the main function for user input and checking if every input is in the correct sequence.
Parameters: none
Return: None
"""
def player():
    player_val = -1
    index = 0
    for index in range(len(game_seq)):
        while not touch1.value and not touch2.value and not touch5.value and not touch6.value:
            pass
        if touch1.value:
            show_pixel((255, 0, 0), 6, 5, .5)
            player_val = 1
            time.sleep(.25)
        if touch2.value:
            show_pixel((0, 255, 0), 9, 8, .5)
            player_val = 0
            time.sleep(.25)
        if touch6.value:
            show_pixel((0, 0, 255), 3, 4, .5)
            player_val = 2
            time.sleep(.25)
        if touch5.value:
            show_pixel((255, 255, 0), 0, 1, .5)
            player_val = 3
            time.sleep(.25)
        if game_seq[index] == player_val:
            index += 1
        else:
            reset()
            break
    time.sleep(.55)

"""
Function: comp
Description: This is the function that generates a random number that will be added to a list. The function will then take
the list, determine which neo pixel to flash, and show the neo pixels.
Parameters: none
Return: None
"""
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


while True:
    if not game_stat:
        if button_a.value:
            button_stat = not button_stat
            time.sleep(.5)
            game_stat = True
    else:
        comp()
        player()
