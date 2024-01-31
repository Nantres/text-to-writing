import pyautogui as gui
import sys
from pynput.mouse import Listener, Controller, Button
from time import sleep

#text = gui.prompt(text='Text to convert:', title='Input Text')
text = input('text: ')

if text == None or text == '':
    sys.exit()
def fontsize_prompt():
    #fontsize = gui.prompt(text='    Font size:\n(no letters, >0)', title='Input Font Size')
    fontsize = input('font size: ')
    if fontsize == None:
        sys.exit()
    elif fontsize == '0':
        ofntsize = fontsize_prompt()
    try:
        int(fontsize)
    except:
        fontsize = fontsize_prompt()
    return float(fontsize)
fontsize = fontsize_prompt()


#gui.alert(text='      Select 2 opposite corners of the area to write in.')
print('select corners')

#select area ====================================================================
selectingarea = True
x_list = []
y_list = []

def on_click(x, y, button, pressed):
    if pressed:
        x_list.append(x)
        y_list.append(y)
    if len(x_list) == 2:
        x_list.sort()
        y_list.sort()
        listener.stop()

with Listener(on_click=on_click) as listener:
    listener.join()

#del x_list, y_list
#=================================================================================
#gui.alert(text='      Press OK, wait 2s for the program to start. \n               *please do not move the cursor')
print('wait 2s')
sleep(2)

#write===========================================================================
mouse = Controller()
line = 0
gui.moveTo(x=x_list[0],y=y_list[0])
characters_dict = {
    'a':(('μ', 16, 91), ('δ', 10, -5), ('δ', 11, -1), ('δ', 9, 0), ('δ', 7, 3), ('δ', 6, 7), ('δ', 2, 11), ('δ', 0, 27), ('δ', 1, 22), ('μ', -5, -37), ('δ', -6, 0), ('δ', -10, 0), ('δ', -9, 2), ('δ', -9, 3), ('δ', -6, 6), ('δ', -2, 7), ('δ', 0, 8), ('δ', 6, 8), ('δ', 12, 3), ('δ', 11, -2), ('δ', 9, -5), ('δ', 6, -6), ('μ', 21, -2), 59),
    'b':(('μ', 20, 49), ('δ', -1, 106), ('μ', 1, -53), ('δ', 11, -10), ('δ', 9, -6), ('δ', 13, -1), ('δ', 9, 4), ('δ', 7, 8), ('δ', 3, 11), ('δ', 1, 12), ('δ', 0, 10), ('δ', -3, 9), ('δ', -4, 9), ('δ', -8, 6), ('δ', -9, 2), ('δ', -9, -1), ('δ', -8, -4), ('δ', -8, -8), ('μ', 64, -42), 88),
    'c':(('μ', 62, 92), ('δ', -10, -6), ('δ', -13, -1), ('δ', -10, 4), ('δ', -7, 5), ('δ', -5, 9), ('δ', -2, 11), ('δ', 0, 14), ('δ', 4, 14), ('δ', 8, 10), ('δ', 10, 4), ('δ', 11, -1), ('δ', 8, -3), ('δ', 6, -4), ('μ', 10, -9), 72),
    'd':(('μ', 69, 48), ('δ', 0, 107), ('μ', 0, -55), ('δ', -13, -11), ('δ', -11, -5), ('δ', -7, -1), ('δ', -9, 4), ('δ', -8, 7), ('δ', -4, 9), ('δ', -1, 8), ('δ', -1, 8), ('δ', 0, 10), ('δ', 3, 9), ('δ', 4, 8), ('δ', 8, 7), ('δ', 12, 2), ('δ', 9, -3), ('δ', 9, -6), ('δ', 9, -9), ('μ', 18, -7), 87),
    'e':(('μ', 67, 150), ('δ', -4, 2), ('δ', -9, 2), ('δ', -9, 1), ('δ', -11, -1), ('δ', -11, -6), ('δ', -6, -9), ('δ', -3, -12), ('δ', 0, -15), ('δ', 2, -10), ('δ', 6, -10), ('δ', 8, -6), ('δ', 12, -3), ('δ', 9, 1), ('δ', 7, 4), ('δ', 7, 8), ('δ', 3, 10), ('δ', 1, 11), ('δ', -7, 0), ('δ', -48, -1), ('μ', 69, -2), 83),
    'f':(('μ', 48, 49), ('δ', -3, -1), ('δ', -7, -1), ('δ', -7, 1), ('δ', -5, 3), ('δ', -3, 5), ('δ', -1, 8), ('δ', -1, 9), ('δ', 0, 80), ('μ', -15, -69), ('δ', 37, 0), ('μ', 7, 2), 50),
    'g':(('μ', 68, 85), ('δ', -18, 0), ('δ', -6, -1), ('δ', -6, -1), ('δ', -6, 0), ('δ', -5, 2), ('δ', -8, 5), ('δ', -4, 8), ('δ', -1, 7), ('δ', 1, 7), ('δ', 4, 8), ('δ', 6, 5), ('δ', 9, 3), ('δ', 9, -1), ('δ', 8, -4), ('δ', 6, -7), ('δ', 2, -11), ('δ', -2, -9), ('δ', -4, -7), ('δ', -4, -3), ('μ', -30, 36), ('δ', -2, 2), ('δ', -3, 5), ('δ', -2, 7), ('δ', 2, 7), ('δ', 6, 4), ('δ', 12, 1), ('δ', 16, 0), ('δ', 10, 3), ('δ', 7, 6), ('δ', 2, 7), ('δ', -2, 7), ('δ', -5, 6), ('δ', -7, 5), ('δ', -9, 2), ('δ', -13, 0), ('δ', -10, -2), ('δ', -8, -5), ('δ', -3, -7), ('δ', 0, -8), ('δ', 4, -6), ('δ', 7, -8), ('μ', 57, -28), 78),
    'h':(('μ', 17, 48), ('δ', 1, 106), ('μ', 0, -54), ('δ', 3, -3), ('δ', 9, -7), ('δ', 8, -5), ('δ', 8, -2), ('δ', 7, 1), ('δ', 5, 3), ('δ', 5, 5), ('δ', 4, 9), ('δ', 1, 7), ('δ', 0, 46), ('μ', 18, -56), 86),
    'i':(('μ', 17, 57), ('δ', 0, 1), ('δ', 1, -1), ('δ', 0, 1), ('μ', 0, 27), ('δ', 0, 68), ('δ', 0, 1), ('μ', 19, -82), 37),
    'j':(('μ', 19, 57), ('δ', 1, 0), ('δ', 0, 1), ('δ', -1, 0), ('μ', 1, 26), ('δ', 0, 82), ('δ', -1, 6), ('δ', -2, 5), ('δ', -4, 4), ('δ', -5, 2), ('δ', -5, 1), ('δ', -3, -1), ('μ', 38, -76), 38),
    'k':(('μ', 19, 48), ('δ', 0, 106), ('μ', 41, -70), ('δ', -30, 30), ('δ', 33, 40), ('μ', 10, -67), 73),
    'l':(('μ', 18, 48), ('δ', 0, 106), ('μ', 20, 0), 38),
    'm':(('μ', 18, 84), ('δ', 1, 70), ('μ', 0, -53), ('δ', 3, -3), ('δ', 9, -8), ('δ', 8, -6), ('δ', 9, -1), ('δ', 7, 2), ('δ', 5, 5), ('δ', 5, 8), ('δ', 1, 8), ('δ', 0, 48), ('μ', 0, -51), ('δ', 4, -5), ('δ', 8, -7), ('δ', 6, -5), ('δ', 7, -3), ('δ', 8, 1), ('δ', 7, 3), ('δ', 5, 6), ('δ', 2, 8), ('δ', 1, 5), ('δ', 0, 49), ('μ', 19, -19), 133),
    'n':(('μ', 18, 84), ('δ', 1, 70), ('μ', 0, -54), ('δ', 7, -5), ('δ', 7, -7), ('δ', 7, -4), ('δ', 9, -1), ('δ', 8, 2), ('δ', 6, 5), ('δ', 4, 9), ('δ', 1, 9), ('δ', 0, 46), ('μ', 20, -14), 88),
    'o':(('μ', 44, 83), ('δ', 0, 0), ('δ', -7, 1), ('δ', -7, 2), ('δ', -5, 4), ('δ', -5, 5), ('δ', -4, 7), ('δ', -2, 8), ('δ', -1, 10), ('δ', 1, 10), ('δ', 3, 9), ('δ', 4, 7), ('δ', 6, 5), ('δ', 9, 3), ('δ', 9, 1), ('δ', 11, -2), ('δ', 7, -5), ('δ', 4, -5), ('δ', 3, -6), ('δ', 3, -8), ('δ', 1, -10), ('δ', -1, -11), ('δ', -2, -8), ('δ', -3, -6), ('δ', -5, -5), ('δ', -5, -3), ('δ', -6, -2), ('δ', -7, -1), ('μ', 43, 35), 88),
    'p':(('μ', 18, 84), ('δ', 1, 100), ('μ', 0, -83), ('δ', 8, -7), ('δ', 8, -7), ('δ', 8, -3), ('δ', 9, -1), ('δ', 8, 3), ('δ', 5, 5), ('δ', 5, 8), ('δ', 2, 10), ('δ', 1, 10), ('δ', 0, 9), ('δ', -2, 6), ('δ', -3, 8), ('δ', -4, 6), ('δ', -5, 4), ('δ', -7, 3), ('δ', -7, 1), ('δ', -7, -2), ('δ', -6, -3), ('δ', -5, -5), ('δ', -8, -7), ('μ', 69, -22), 88),
    'q':(('μ', 69, 84), ('δ', 0, 100), ('μ', -1, -85), ('δ', -4, -3), ('δ', -9, -7), ('δ', -8, -5), ('δ', -10, -1), ('δ', -8, 3), ('δ', -6, 4), ('δ', -4, 7), ('δ', -3, 7), ('δ', -2, 9), ('δ', -1, 7), ('δ', 1, 8), ('δ', 2, 8), ('δ', 3, 8), ('δ', 6, 6), ('δ', 7, 4), ('δ', 9, 1), ('δ', 7, -1), ('δ', 6, -4), ('δ', 5, -5), ('δ', 9, -7), ('μ', 19, 2), 87),
    'r':(('μ', 18, 84), ('δ', 1, 71), ('μ', 0, -53), ('δ', 3, -3), ('δ', 8, -8), ('δ', 7, -6), ('δ', 6, -2), ('δ', 5, 1), ('δ', 3, 1), ('μ', 7, 21), 58),
    's':(('μ', 50, 87), ('δ', -5, -2), ('δ', -7, -3), ('δ', -8, 0), ('δ', -6, 2), ('δ', -4, 3), ('δ', -4, 5), ('δ', -2, 7), ('δ', 2, 7), ('δ', 4, 5), ('δ', 7, 4), ('δ', 13, 5), ('δ', 7, 4), ('δ', 4, 6), ('δ', 2, 7), ('δ', -2, 6), ('δ', -4, 6), ('δ', -7, 4), ('δ', -9, 2), ('δ', -8, -1), ('δ', -7, -3), ('δ', -5, -3), ('μ', 54, -8), 65),
    't':(('μ', 22, 64), ('δ', 0, 74), ('δ', 1, 7), ('δ', 3, 6), ('δ', 6, 3), ('δ', 6, 1), ('δ', 5, -1), ('δ', 3, -1), ('μ', -39, -68), ('δ', 39, 0), ('μ', 10, 13), 56),
    'u':(('μ', 18, 83), ('δ', 1, 51), ('δ', 3, 10), ('δ', 5, 6), ('δ', 5, 3), ('δ', 7, 2), ('δ', 7, -1), ('δ', 7, -4), ('δ', 6, -5), ('δ', 9, -8), ('μ', 0, -53), ('δ', 1, 69), ('μ', 19, -21), 88),
    'v':(('μ', 10, 84), ('δ', 25, 67), ('δ', 2, 2), ('δ', 2, -2), ('δ', 26, -67), ('μ', 9, 16), 74),
    'w':(('μ', 11, 85), ('δ', 22, 68), ('δ', 3, 0), ('δ', 2, -2), ('δ', 19, -66), ('δ', 2, 0), ('δ', 21, 69), ('δ', 2, 0), ('δ', 3, -1), ('δ', 21, -68), ('μ', 11, 15), 117),
    'x':(('μ', 12, 84), ('δ', 47, 70), ('μ', -49, 1), ('δ', 49, -71), ('μ', 10, 51), 69),
    'y':(('μ', 9, 84), ('δ', 28, 73), ('μ', 28, -73), ('δ', -37, 99), ('μ', 46, -11), 74),
    'z':(('μ', 13, 85), ('δ', 38, 0), ('δ', 0, 2), ('δ', 0, 2), ('δ', -38, 61), ('δ', -1, 3), ('δ', 43, 0), ('μ', 12, -25), 67),
    ' ':(('μ', 38, 63), 38),
    ',':(('μ', 21, 148), ('δ', 3, 0), ('δ', 0, 6), ('δ', -3, 0), ('δ', 0, -6), ('μ', 3, 7), ('δ', -14, 22), ('δ', 12, -22), ('μ', 21, -16), 41),
    '.':(('μ', 18, 148), ('δ', 4, 0), ('δ', 0, 6), ('δ', -4, 0), ('δ', 0, -6), ('δ', 2, 3), ('μ', 22, -4), 42)
    }

for char in text:
    if gui.position()[0] + int(characters_dict[char][-1]/100*fontsize) > x_list[1]:
            mouse.position = (x_list[0],y_list[0])
            line += 1
    sleep(0.05)
    mouse.position = (gui.position()[0],int(y_list[0]+line*2.06*fontsize))
    for data in characters_dict[char]:
        try:
            if data[0] == "δ":
                mouse.press(Button.left)
                mouse.move(int(data[1]/100*fontsize),int(data[2]/100*fontsize))
                mouse.release(Button.left)
                sleep(0.05)
            elif data[0] == "μ":
                mouse.move(int(data[1]/100*fontsize),int(data[2]/100*fontsize))
                sleep(0.05)
        except TypeError:
            pass
        