import Intersection_Manager_class as IMC
import Car_Class as CC
import turtle
import random
import csv



manager = IMC.Intersection_Manager()
list_car_data = []
pastLane = None
startTime = 0
timeLimit = 100 #seconds
numberOfCars = 25
speedLimit = 35
maxSpeed = 40 # not used
minSpeed = 20 # not used





#set up csv writer
f = open('carData.csv', 'wb')
w = csv.writer(f)

def clearFile():
    file = open('carData.csv', 'wb')
    file.truncate()

def addLine(data):
    w.writerow(data)

#clear old data
clearFile()

#generate cars
cars = []

for i in range(numberOfCars):
    # generate data
    vin = i
    lane = random.randint(1, 4)
    delay = random.randrange(750, 1000, 1)
    speed = random.randrange(3000, 3100, 1) / 100.00
    accel = random.randrange(-20, 20, 1) / 100.0
    turn = random.randint(0, 1)
    lenth = random.randrange(20, 30, 1) / 10.0
    width = random.randrange(10, 20, 1) / 10.0

    if pastLane == lane:
        delay = 1200
    startTime = startTime + delay
    PastLane = lane

    # create car
    test_car = CC.Car(vin, speed, accel, startTime, lane, turn, lenth, width)
    cars.append(test_car)




"""
vin = 1
lane = 1
delay = 0
speed = 35
accel = 0 #random.randrange(-1, 1, 1) / 10.0
turn = 0 #random.randint(0, 1)
lenth = 2.5#random.randrange(20, 30, 1) / 10.0
width = 1.5#random.randrange(10, 20, 1) / 10.0

startTime = startTime + delay

# create car
test_car = CC.Car(vin, speed, accel, startTime, lane, turn, lenth, width)
cars.append(test_car)


vin = 2
lane = 2
delay = 900
speed = 37
accel = 0 #random.randrange(-1, 1, 1) / 10.0
turn = 0 #random.randint(0, 1)
lenth = 2.5#random.randrange(20, 30, 1) / 10.0
width = 1.5#random.randrange(10, 20, 1) / 10.0

startTime = startTime + delay

# create car
test_car = CC.Car(vin, speed, accel, startTime, lane, turn, lenth, width)
cars.append(test_car)
"""


#generate header VIN, Lane, length, width
header = []
for i in range(4):
    for C in cars:
        if i == 0:
            header.append(C.vin)
        elif i == 1:
            header.append(C.lane)
        elif i == 2:
            header.append(C.length)
        elif i == 3:
            header.append(C.width)
    addLine(header)
    header = []


#insert each car and get updated accel value
for C in cars:
    C.updateAccel01(manager.addReservation(C.generatereservation()))

#get positioning and check for needing outro
positionsX = []
positionsY = []
currentTime = 0
while (currentTime < timeLimit * 1000):

    for C in cars:
        #check if completed p2  (combine these two checks please)
        if C.expectedTime01 <= currentTime and C.set == 0:  #
            C.set = 1
            C.updateAccel1(manager.bookOutro(C.generatereservationOUT()))
        #check for done with interection
        if C.checkForDone(currentTime) and C.set == 1:
            positionsX.append(0)
            positionsY.append(0)
        else:
            delta = C.distanceTravelledTime(currentTime)
            positionsX.append(delta[0])
            positionsY.append(delta[1])

    """
    i = 0
    while i < len(cars):
        C = cars[i]

        if C.expectedTime01 <= currentTime and C.set == 0:  # has car passed through middle
            C.set = 1
            C.updateAccel1(manager.bookOutro(C.generatereservationOUT()))


        delta = C.distanceTravelledTime(currentTime)
        positionsX.append(delta[0])
        positionsY.append(delta[1])

        if C.checkForDone(currentTime) and C.set == 1:
            cars.remove(C)
        else:
            i = i + 1
    """
    addLine(positionsX)
    addLine(positionsY)
    positionsX = []
    positionsY = []
    currentTime = currentTime + 1


manager.toString()
