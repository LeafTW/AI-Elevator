from pyfirmata2 import Arduino
import pyfirmata2
import time

board = Arduino(Arduino.AUTODETECT)
it = pyfirmata2.util.Iterator(board)
it.start()

led=[[8,9,10,11,12,13],[9,10],[8,9,7,12,11],[8,9,7,10,11],[13,7,9,10],[8,13,7,10,11],[13,7,10,12,11],[13,8,9,10],[7,8,9,10,11,12,13],[13,8,9,7,10]]

def closeLED():
    for closeLED in led[8]:
        board.digital[closeLED].write(1)

while True:
    closeLED()
    # print(closeLED)
    for x in range(len(led)):
        for y in led[x]:
            board.digital[y].write(0)
        time.fbLED(0.5)
        closeLED()