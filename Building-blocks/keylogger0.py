#!/usr/binenv python
import pynput

def process_key_process(key):
    print(key)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_process)

with keyboard_listener:
    keyboard_listener.join()
