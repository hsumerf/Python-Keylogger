from threading import Timer
def hello():
    print "hello, world"

def umer():
    print "hello, umer"

while True:
    t1 = Timer(1.0, hello)
    t2 = Timer(1.0, umer)
    t1.start()  # after 30 seconds, "hello, world" will be printed

    t2.start()  # after 30 seconds, "hello, world" will be printed
