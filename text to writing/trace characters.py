from pynput.mouse import Button, Listener as m_Listener
from time import sleep
start = []
x_list = []
y_list = []
command_list = []
#char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','']
chars = 'ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-`~[]:;\'",.<>/?'
char_list = []
for i in chars:
    char_list.append(str(i))
def on_click(x, y, button, pressed):
    if len(start) == 0:
        start.append(x)
        start.append(y)
        x_list.append(x)
        y_list.append(y)
        print(start)
        return
    
    if pressed:
        if button == Button.left or button == Button.right:
            x_list.append(x)
            y_list.append(y)
        if button == Button.left:
            command_list.append(("δ",x_list[-1]-x_list[-2],y_list[-1]-y_list[-2]))
        if button == Button.right:
            command_list.append(("μ",x_list[-1]-x_list[-2],y_list[-1]-y_list[-2]))
        if button == Button.middle:
            command_list.append(x_list[-1]-x_list[0])
            print("'{0}':{1}".format(char_list[0],tuple(command_list)))
            char_list.pop(0)
            x_list.clear()
            y_list.clear()
            command_list.clear()
            x_list.append(start[0])
            y_list.append(start[1])
            
            

        

def get(button,x,y):
    #drag is δa, move is μa
    string = ''
        

# Collect events until released
with m_Listener(on_click=on_click) as listener2:
    listener2.join()

