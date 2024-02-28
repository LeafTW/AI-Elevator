from pyfirmata2 import Arduino
import pyfirmata2
import time

board = Arduino(Arduino.AUTODETECT)
it = pyfirmata2.util.Iterator(board)
it.start()

load = 2; # PL pin 1
clockEnablePin = 3; # CE pin 15
dataIn = 5; # Q7 pin 7
clockIn = 4; #CP pin 2
ansData=''
InputButten=16

board.digital[dataIn].mode = pyfirmata2.INPUT
class staticInt:
    ansData=''

while True:
    staticInt.ansData=''
    board.digital[load].write(0)
    time.sleep(0.005)
    board.digital[load].write(1)
    time.sleep(0.005)

    # Get data from 74HC165
    # board.digital[clockIn].write(1)
    board.digital[clockEnablePin].write(0)
    for i in range(0,InputButten):
        # if i<=7:
        staticInt.ansData=staticInt.ansData+str('{}: {} '.format(i,board.digital[dataIn].read()))
        # else:
        #     staticInt.ansData = staticInt.ansData + str('{}: {} '.format(i,not board.digital[dataIn].read()))
        # print(voidDataIn())
        board.digital[clockIn].write(0)
        time.sleep(0.005)
        board.digital[clockIn].write(1)
        time.sleep(0.005)
    board.digital[clockEnablePin].write(1)
    print(staticInt.ansData)