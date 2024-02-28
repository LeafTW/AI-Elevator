import control_arduino
import time
import AI_photo
import AI_camera

tEnd = 0        #時間延遲變數
movetime = 2    #電梯移動速度
OpCotime = 5   #電梯開關速度
waitMachineTime = 15 #電梯等待時間不超過?
inElevatorPeople=5 #電梯內不超過?人
doorstate=0


class elevator:
    buttenLED=[]
    def __init__(self,machineNumber):
            self.machineNumber=machineNumber
            self.__machineoder=[]
            self.__machineOderPeople=[]
            self.machineState=3
            self.machineAdress=0
            self.doorstate=0
            self.timeDelay=0
            self.inElevatorPeople=0

    @property
    def inElevatorPeople(self):
        return self.__tinElevatorPeople

    @inElevatorPeople.setter
    def inElevatorPeople(self, value):
        self.__inElevatorPeople = value

    @property
    def timeDelay(self):
        return self.__timeDelay

    @timeDelay.setter
    def timeDelay(self, value):
        self.__timeDelay = value

    @property
    def doorstate(self):
        return self.__doorstate

    @doorstate.setter
    def doorstate(self, value):
        self.__doorstate = value

    @property
    def machineOderPeople(self):
        return self.__machineOderPeople

    @machineOderPeople.setter
    def machineOderPeople(self, value):
        self.__machineOderPeople = value

    @property
    def machineoder(self):
        return self.__machineoder

    @machineoder.setter
    def machineoder(self, value):
        self.__machineoder= value

    @property
    def machineAdress(self):
        return self.__machineAdress

    @machineAdress.setter
    def machineAdress(self, value):
        self.__machineAdress = value

    @property
    def machineState(self):
        return self.__machineState

    @machineState.setter
    def machineState(self,value):
        if value > 3:
            raise ValueError("Car machineState cannot >3")
        self.__machineState = value

def initialization(buttenList):
    Range=range(buttenList)
    for i in Range:
        elevator.buttenLED.append(0)

def howManyState(machineList,callFloor,searchNumber): #輸入機台陣列/樓層位置/查詢狀態
    stateList=[]
    for machineNumber in machineList:
        if machineNumber.machineState==searchNumber:
            stateList.append(machineNumber)
        elif (machineNumber.machineState==searchNumber) & (machineNumber.machineAdress < callFloor):
            stateList.append(machineNumber)
        elif (machineNumber.machineState==searchNumber) & (machineNumber.machineAdress > callFloor):
            stateList.append(machineNumber)
    return stateList #符合條件機台

def whichIsRecent(machineList,callFloor,searchItem):
    recent=999
    if searchItem == "machine":
        for getMachineList in machineList:
            # print(machineList[getMachineList].machineState)
            if abs(getMachineList.machineAdress-callFloor)<recent:
                recent=abs(getMachineList.machineAdress-callFloor)
                whichIsRecentMachine=getMachineList
    elif searchItem == "oder":
        for getMachineList in machineList:
            if len(getMachineList.machineoder) < recent:
                recent=len(getMachineList.machineoder)
                whichIsRecentMachine=getMachineList
    # print(whichIsRecentMachine)
    return whichIsRecentMachine

def runMachine(machineList):
    print7LED=[0 for _ in range(len(machineList))]
    for getMachineList in range(len(machineList)):
        # print(getMachineList)
        if len(machineList[getMachineList].machineoder) == 0:
            # print('runMachine0')
            print7LED[getMachineList] = machineList[getMachineList].machineAdress
            # machineList[getMachineList].machineState = 3
            continue
        elif machineList[getMachineList].machineAdress == int(machineList[getMachineList].machineoder[0]/2):
            # print('runMachine1')
            print7LED[getMachineList]=machineList[getMachineList].machineAdress
            # machineList[getMachineList].machineState = 3
            continue
        elif machineList[getMachineList].machineAdress > int(machineList[getMachineList].machineoder[0]/2) :
            if millis(movetime,machineList[getMachineList]) == False:
                # print('runMachine2-1')
                print7LED[getMachineList] = machineList[getMachineList].machineAdress
                changeState(machineList[getMachineList])
                continue
            # print('runMachine2-2')
            print7LED[getMachineList] = machineList[getMachineList].machineAdress - 1
            machineList[getMachineList].machineAdress= machineList[getMachineList].machineAdress - 1
            changeState(machineList[getMachineList])
            continue
        elif machineList[getMachineList].machineAdress < int(machineList[getMachineList].machineoder[0]/2):
            if millis(movetime,machineList[getMachineList]) == False:
                # print('runMachine3-1')
                print7LED[getMachineList] = machineList[getMachineList].machineAdress
                changeState(machineList[getMachineList])
                continue
            # print('runMachine3-2')
            print7LED[getMachineList] = machineList[getMachineList].machineAdress + 1
            machineList[getMachineList].machineAdress = machineList[getMachineList].machineAdress + 1
            changeState(machineList[getMachineList])
            continue
    # print("runmachine")
    # print(print7LED)
    # print()
    return print7LED

def show7LED(Print7LED,machineList):
    finalPrintList=[]
    for getMachineList in range(len(machineList)):
        # print(machineList[getMachineList].machineOderPeople)
        led = [[1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 0, 1, 0],
               [0, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 1, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 1, 1, 0]]  # LED 0～9/全關
        if len(machineList[getMachineList].machineoder) ==0:
            # print('show0')
            finalPrintList.append(led[machineList[getMachineList].machineAdress])
        elif (int(machineList[getMachineList].machineoder[0]/2)==machineList[getMachineList].machineAdress) & (
                machineList[getMachineList].doorstate==0):
            machineList[getMachineList].doorstate =1
            led[Print7LED[getMachineList]][7]=1 #doorOpen
            finalPrintList.append(led[Print7LED[getMachineList]])
            millis(OpCotime,machineList[getMachineList])
            # print('show1')
            continue
        elif machineList[getMachineList].doorstate == 1 :
            if millis(OpCotime,machineList[getMachineList])==False:
                led[Print7LED[getMachineList]][7] = 1  # doorOpen
                finalPrintList.append(led[Print7LED[getMachineList]])
                # print('show2-1')
                continue
            if inElevatorPeopleIF(machineList[getMachineList]):
                machineList[getMachineList].doorstate = 0
                finalPrintList.append(led[Print7LED[getMachineList]])
                elevator.buttenLED[machineList[getMachineList].machineoder[0]] = 0
                del machineList[getMachineList].machineoder[0]
                del machineList[getMachineList].machineOderPeople[0]
                printMachineAdress(machineList)
                # machineList[getMachineList].machineState = 3
                if len(machineList[getMachineList].machineoder) == 0:
                    machineList[getMachineList].machineState = 3
                # print('show2-2')
                continue
        elif int(machineList[getMachineList].machineoder[0]/2) != machineList[getMachineList].machineAdress:
            machineList[getMachineList].doorstate = 0
            # print(Print7LED[getMachineList])
            finalPrintList.append(led[Print7LED[getMachineList]])
            # print('show3')
            continue
    # print(finalPrintList)
    finalPrintList.append(elevator.buttenLED)
    control_arduino.runIC.IC_74HC595(finalPrintList)
    # print(finalPrintList)

def inElevatorPeopleIF(machinelist):
    # searchAns=AI_camera.start()
    machinelist.inElevatorPeople=AI_photo.star()
    print("電梯內人數:{}".format(machinelist.inElevatorPeople))
    # searchAns=input()
    # searchAns=int(searchAns)
    if machinelist.inElevatorPeople > inElevatorPeople:
        control_arduino.runIC.buzzer(True)
        return False
    else:
        control_arduino.runIC.buzzer(False)
        return True

def pending(ButtenList,machineList):
    returnPending=[]
    returnPendingValue=True
    for get7416Data in control_arduino.get7416Data(ButtenList):
        YESorNO=True
        for getButtenList in machineList:
            if YESorNO == False:
                continue
            for getButtenListNumber in getButtenList.machineoder:
                if getButtenListNumber == get7416Data:
                    # print("run0")
                    YESorNO = False
                    break
        for ReturnPendingValue in returnPending:
            if ReturnPendingValue == get7416Data:
                # print("run1")
                returnPendingValue=False
        if YESorNO & (returnPendingValue==True):
            # print("run0")
            returnPending.append(get7416Data)
    return returnPending

def changeState(machienList):
    if (machienList.machineoder[0] % 2) == 0:
        machienList.machineState = 1
    elif (machienList.machineoder[0] % 2) == 1:
        machienList.machineState = 2

def millis(timeDelay,machineList):
    tEnd=machineList.timeDelay
    if tEnd == 0:
        machineList.timeDelay=round(time.time())
        return True
    if round(time.time()) - tEnd >= timeDelay:
        machineList.timeDelay=round(time.time())
        return True
    elif round(time.time()) - tEnd < timeDelay:
        return False

def cameraSearch_oderAppend(machine,Pending,machineList):
        machine.machineoder.append(Pending)
        machine.machineOderPeople.append([Pending,(AI_photo.star()),round(time.time())])
        printMachineAdress(machineList)
        elevator.buttenLED[Pending]=1

def sortMachine(machineList):
    # needprint=0 #如果超時print oder狀態
    for getmachineList in machineList:
        changeOderAdress=1 #要更換oder位置變數
        checkData = []
        if len(getmachineList.machineoder) < 3:
            continue
        #抓要排序的DATA
        for sortData in range(1,len(getmachineList.machineOderPeople)):
            checkData.append(getmachineList.machineOderPeople[sortData])
        checkData.sort(key=lambda checkData: checkData[2]) #以時間排序
        for checkDataNumber in checkData:#檢查時間是否超時
            if (round(time.time())-checkDataNumber[2]) > waitMachineTime:
                # print("run0")
                # print("time {} Address{}".format(checkDataNumber[0],changeOderAdress),end="/")
                getmachineList.machineoder[changeOderAdress ] = checkDataNumber[0]
                getmachineList.machineOderPeople[changeOderAdress] = checkDataNumber
                del checkData[changeOderAdress-1]
                changeOderAdress=changeOderAdress+1
                # needprint+=1
                continue
            break
        if len(checkData) != 0:
            checkData.sort(reverse=True, key=lambda checkData: checkData[1])#以人數多寡排序
            # print(getmachineList.machineoder)
            # print(getmachineList.machineOderPeople)
            # returnData.append(checkData)
            for setOder in range(len(checkData)):
                # print("People {} Address{}".format(checkData[setOder][0],changeOderAdress),end="/")
                getmachineList.machineoder[changeOderAdress]=checkData[setOder][0]
                getmachineList.machineOderPeople[changeOderAdress] = checkData[setOder]
                changeOderAdress=changeOderAdress+1

def printMachineAdress(machineList):
    for getmachineList in machineList:
        print("Number:{} ".format(getmachineList.machineNumber),end="")
        # print(getmachineList.machineOderPeople)
        for getOder in getmachineList.machineoder:
            for getmachineOderPeople in getmachineList.machineOderPeople:
                if getOder == getmachineOderPeople[0]:
                    if (getOder % 2) == 0:
                        print("Up:{} People:{} time:{}"
                              .format(int(getmachineOderPeople[0] / 2),getmachineOderPeople[1],round(time.time())-(getmachineOderPeople[2])), end=" / ")
                    else:
                        print("Down:{} People:{} time:{}"
                              .format(int(getmachineOderPeople[0] / 2),getmachineOderPeople[1],round(time.time())-(getmachineOderPeople[2])), end=" / ")
        print()
    print("----------------------------------------")


