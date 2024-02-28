from pyfirmata2 import Arduino
import pyfirmata2
import time

board = Arduino(Arduino.AUTODETECT)
it = pyfirmata2.util.Iterator(board)
it.start()
led = [[1, 1, 1, 1, 1, 1, 0, 0], [0 ,1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 0, 1, 1],
       [0, 1, 1, 0, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1]] # LED 0～9/全關
latchPin = 7; #ST_CP pin 12
clockPin = 6; #SH_CP pin 11
dataPin = 8; #DS pin 14

ts1=[1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 0, 0,
]


for ledTotle in range(len(ts1)):
    board.digital[latchPin].write(0)
    # print(led[0][i])
    board.digital[clockPin].write(0)
    board.digital[dataPin].write(not ts1[ledTotle])
    time.sleep(0.005)
    board.digital[clockPin].write(1)
    time.sleep(0.005)
    # board.digital[clockPin].write(0)
board.digital[latchPin].write(1)


# while True:
#     for ledTotle in range(len(led)):
#         board.digital[latchPin].write(0)
#         for i in range(7,-1,-1):
#             # print(led[0][i])
#             board.digital[clockPin].write(0)
#             print(i)
#             board.digital[dataPin].write(not led[ledTotle][i])
#             time.sleep(0.005)
#             board.digital[clockPin].write(1)
#             time.sleep(0.005)
#         # board.digital[clockPin].write(0)
#         board.digital[latchPin].write(1)
#         time.sleep(0.5)