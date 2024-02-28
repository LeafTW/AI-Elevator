import AI_Elevator
import control_arduino

Pending=[]
ButtenList= 16    #按鈕數量

machineList=[AI_Elevator.elevator("A"), AI_Elevator.elevator("B")]
AI_Elevator.initialization(ButtenList)

#---------------test----------------
machineList[0].machineAdress=7
# Pending=[11,6,9,10,5,14,1]
# Pending=[4,13,9,10,7,14,1,2,11,6,3,8,5,12,15,0]

while True:
    Pending=AI_Elevator.pending(ButtenList, machineList)
    if len(Pending)!=0:
        callFloor=int(Pending[0]/2)
        callFloorNumber=Pending[0]%2 #0是上升按鈕 1是下降按鈕
        if len(Pending)>0:
            # 電梯狀態 1:stateUp 2:stateDown 3:stateStany
            state3Ans=AI_Elevator.howManyState(machineList, callFloor, 3)
            state2Ans = AI_Elevator.howManyState(machineList, callFloor, 2)
            state1Ans = AI_Elevator.howManyState(machineList, callFloor, 1)
            if len(state3Ans)==1:
                recentMachine=state3Ans[0]
                AI_Elevator.cameraSearch_oderAppend(recentMachine, Pending[0], machineList)
                # print('run0')
            elif len(state3Ans)>0:
                # print('run1')
                recentMachine=AI_Elevator.whichIsRecent(state3Ans, callFloor, "machine")
                AI_Elevator.cameraSearch_oderAppend(recentMachine, Pending[0], machineList)
            elif callFloorNumber == 1 :
                if len(state2Ans) ==0 :
                    recentMachine = AI_Elevator.whichIsRecent(machineList, callFloor, "oder")
                    AI_Elevator.cameraSearch_oderAppend(recentMachine, Pending[0], machineList)
                    # print('run2-1')
                    continue
                # print('run2-2')
                recentMachine=AI_Elevator.whichIsRecent(state2Ans, callFloor, "machine")
                AI_Elevator.cameraSearch_oderAppend(recentMachine, Pending[0], machineList)
            elif callFloorNumber == 0:
                if len(state1Ans) == 0:
                    recentMachine = AI_Elevator.whichIsRecent(machineList, callFloor, "oder")
                    AI_Elevator.cameraSearch_oderAppend(recentMachine, Pending[0], machineList)
                    # print('run3-1')
                    continue
                # print('run3-2')
                recentMachine = AI_Elevator.whichIsRecent(state1Ans, callFloor, "machine")
                AI_Elevator.cameraSearch_oderAppend(recentMachine, Pending[0], machineList)

    AI_Elevator.sortMachine(machineList)
    printLED=AI_Elevator.runMachine(machineList)
    AI_Elevator.show7LED(printLED, machineList)
    if len(Pending) !=0:
        Pending.pop(0)

