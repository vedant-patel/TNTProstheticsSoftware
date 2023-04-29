import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from pyfirmata import Arduino, SERVO, util
from time import sleep

"""
port = 'COM3'
board = Arduino(port)

servo0 = 5  # Index
servo1 = 6  # Middle
servo2 = 10  # Ring
servo3 = 9  # Pinky
servo4 = 6  # Thumb

board.digital[servo0].mode = SERVO
board.digital[servo1].mode = SERVO
board.digital[servo2].mode = SERVO
board.digital[servo3].mode = SERVO
# board.digital[servo4].mode = SERVO
# board.digital[servo5].mode = SERVO

da = 5
angle = 0

def clench_finger(angle,servonum):
    if angle + da < 180:
            angle = angle + da
            board.digital[servonum].write(angle)
            sleep(SERVO_DELAY)

def unclench_finger(angle, servonum):
    if angle - da > 0:
            angle = angle - da
            board.digital[SERVO0].write(angle)
            sleep(SERVO_DELAY)
"""


def index(request):
    return render(request, 'index.html')


# Create your views here.
def moveFinger(pin, angle):
    for i in range(0, angle):
        board.digital[pin].write(i)
        sleep(0.005)
    for i in range(angle, 0, -1):
        board.digital[pin].write(i)
        sleep(0.005)


def indexFinger(val):
    # moveFinger(servo0, val)
    print(val)


def middleFinger(val):
    # moveFinger(servo1, val)
    print(val)


def ringFinger(val):
    # moveFinger(servo2, val)
    print(val)


def pinkyFinger(val):
    # moveFinger(servo3, val)
    print(val)


def thumbFinger(val):
    # moveFinger(servo4, val)
    print(val)


def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        index = int(data['index'])
        middle = int(data['middle'])
        ring = int(data['ring'])
        pinky = int(data['pinky'])
        thumb = int(data['thumb'])
        indexFinger(index)
        middleFinger(middle)
        ringFinger(ring)
        pinkyFinger(pinky)
        thumbFinger(thumb)
        return JsonResponse(data, safe=False)
