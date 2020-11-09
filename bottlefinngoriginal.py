import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

sensor = 4
led = 27
obj= 0

TRIG = 17
ECHO = 18
i=0

motor1 = 22
motor2 = 25

pump = 26

GPIO.setup(motor1,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(pump,GPIO.OUT)

GPIO.output(TRIG, False)
GPIO.output(led,False)
GPIO.output(motor1,False)
GPIO.output(motor2,False)
GPIO.output(pump,False)

print("place object")
def obj_detc():
if GPIO.input(sensor):
GPIO.output(led,False)
obj = 0 # place the object

    else:
    GPIO.output(led,True)
        obj = 1 # object is detected
            
return obj
def level():

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
       pulse_start = time.time()

    while GPIO.input(ECHO)==1:
       pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance+1.15, 2)
return distance
try:
    while True :
        obj= obj_detc()
	if obj :
            print "object detected"
	    GPIO.output(motor1,False)
	    GPIO.output(motor2,False)

            distance = level()

            if distance<=15 and distance>=5 and obj==True:
                print "sufficient liquid was filled"
                print "liquid level is:",distance,"cm"
                #i=0
                GPIO.output(pump,True)
                GPIO.output(motor1,True)
                GPIO.output(motor2,False)
                time.sleep(2)
            elif distance>15 and obj==True :
                print "liquid level is:",distance,"cm"
                #i=1
                print "suficient liquid is not filled"
                GPIO.output(pump,False)

	else :
            print "place the object"
            GPIO.output(motor1,True)
            GPIO.output(motor2,False)
            GPIO.output(pump,True)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()

