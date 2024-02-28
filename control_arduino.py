from pyfirmata2 import Arduino
import pyfirmata2
import time

readflst = []

buzzerPin=9
#------------------IC_74HC595---------------------
latchPin = 7; #ST_CP pin 12
clockPin = 6; #SH_CP pin 11
dataPin = 8; #DS pin 14

#------------------IC_74HC165---------------------
load = 2; # PL pin 1
clockEnablePin = 3; # CE pin 15
dataIn = 5; # Q7 pin 7
clockIn = 4; #CP pin 2

board = Arduino(Arduino.AUTODETECT)
it = pyfirmata2.util.Iterator(board)
it.start()
board.digital[dataIn].mode = pyfirmata2.INPUT

class runIC:
    def IC_74HC595(printLedList):
        board.digital[latchPin].write(0)
        for showLedList in range(len(printLedList)-1,-1,-1):
            for i in range(len(printLedList[showLedList])-1, -1, -1):
                board.digital[clockPin].write(0)
                board.digital[dataPin].write(not printLedList[showLedList][i])
                time.sleep(0.005)
                board.digital[clockPin].write(1)
                time.sleep(0.005)
            # board.digital[clockPin].write(0)
            # print(showLedList)
        board.digital[latchPin].write(1)

    def IC_74HC165(howManyButten):
        board.digital[load].write(0)
        time.sleep(0.005)
        board.digital[load].write(1)
        time.sleep(0.005)
        board.digital[clockEnablePin].write(0)
        for i in range(0, howManyButten):
            readflst.append(False)
            board.digital[clockIn].write(1)
            readflst[i]=not board.digital[dataIn].read()
            # print('{}:{}'.format(i,str(readflst[i])),end='')
            # elif readflst[i] == False:
            #     readflsteadflst[i] = board.digital[dataIn].read()
            time.sleep(0.009)
            board.digital[clockIn].write(0)
        # print("run74165")
        board.digital[clockEnablePin].write(1)
        return readflst

    def buzzer(close_open):
        if close_open == True:
            board.digital[buzzerPin].write(1)
        else:
            board.digital[buzzerPin].write(0)

def get7416Data(howManyButten):
    returnValue=[]
    value=runIC.IC_74HC165(howManyButten)
    for number in range(len(value)):
        if value[number]==True:
            returnValue.append(number)
    return returnValue


