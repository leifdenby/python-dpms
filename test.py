from gpiozero import Button
from time import sleep

import subprocess

button = Button(17)

screen_on = True

# d = dpms.DPMS() # to use the current display, or alternatively DPMS(":1")

# d.Enable()


while True:
    if button.is_pressed:
        if not screen_on:
            subprocess.call("xset dpms force off".split())
            screen_on = True
        print("Pressed")
    else:
        if screen_on:
            subprocess.call("xset dpms force on".split())
            screen_on = False
        print("Released")
    sleep(0.5)
