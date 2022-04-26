from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO 
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led1 = LED(17)
led2 = LED(14)
led3 = LED(26)


### GUI DEFINITIONS ###
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTONS ###


def ledToggles():
    if led1.is_lit:
        led1.off()
        ledButton["text"] = "turn red LED on"
    else:
            led1.on()
            led2.off()
            led3.off()
            ledButton["text"] = "turn red LED off"
            ledButton2["text"] = "turn blue LED on"
            ledButton3["text"] = "turn orange LED on"

def ledToggle():
    if led2.is_lit:
        led2.off()
        ledButton2["text"] = "turn blue LED on"
    else:
            led2.on()
            led1.off()
            ledButton["text"] = "turn red LED on"
            led3.off()
            ledButton3["text"] = "turn orange LED on"
            ledButton2["text"] = "turn blue LED off"
        

            
def ledToggless():
    if led3.is_lit:
        led3.off()
        ledButton3["text"] = "turn orange LED on"
    else:
            led3.on()
            led1.off()
            led2.off()
            ledButton3["text"] = "turn orange LED off"
            ledButton["text"] = "turn red LED on"
            ledButton2["text"] = "turn blue LED on"
                        
            
def close():
        RPi.GPIO.cleanup()
        win.destroy()
  
        
        
### WIDGETS ###
ledButton = Button(win, text = 'turn red LED on', font = myFont, command = ledToggles, bg = 'red', height = 1, width = 24)
ledButton.grid(row=0,column=1)

ledButton2 = Button(win, text = 'turn blue LED on', font = myFont, command = ledToggle, bg = 'blue', height = 1, width = 24)
ledButton2.grid(row=1,column=1)

ledButton3 = Button(win, text = 'turn orange LED on', font = myFont, command = ledToggless, bg = 'orange', height = 1, width = 24)
ledButton3.grid(row=2,column=1)

ExitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
ExitButton.grid(row=3,column=1)

 
