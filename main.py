import RPi.GPIO as GPIO
import time
import face_det
import os

LED_PIN=18
LINKIT_IN_HOLD=22
LINKIT_IN_STOP=23
LINKIT_IN_MUS_1=6
LINKIT_IN_MUS_2=12

LINKIT_OUT_0=4
LINKIT_OUT_1=14
PWM_FREQ=200
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LINKIT_OUT_0,GPIO.OUT)
GPIO.setup(LINKIT_OUT_1,GPIO.OUT)

GPIO.setup(LINKIT_IN_HOLD, GPIO.IN)
GPIO.setup(LINKIT_IN_STOP, GPIO.IN)
GPIO.setup(LINKIT_IN_MUS_1, GPIO.IN)
GPIO.setup(LINKIT_IN_MUS_2, GPIO.IN)

state=0
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.output(LINKIT_OUT_0, GPIO.LOW)
GPIO.output(LINKIT_OUT_1, GPIO.LOW)

try:
	while True:
		print("現在模式：", state)
		if state==0:
			os.system("python2 play0.py")
			GPIO.output(LINKIT_OUT_0, GPIO.LOW)
			GPIO.output(LINKIT_OUT_1, GPIO.LOW)
			GPIO.output(LED_PIN, GPIO.LOW)	
			state = face_det.face_det()
			if state == 1:
				GPIO.output(LINKIT_OUT_0, GPIO.LOW)
				GPIO.output(LINKIT_OUT_1, GPIO.HIGH)
				os.system("python2 play1.py")
				time.sleep(0.5)
			elif state == 2:
				GPIO.output(LINKIT_OUT_0, GPIO.HIGH)
				GPIO.output(LINKIT_OUT_1, GPIO.LOW)
				time.sleep(0.5)
				os.system("python2 play2.py")
		
		elif state==1:
			GPIO.output(LED_PIN,GPIO.HIGH)
			GPIO.output(LINKIT_OUT_0, GPIO.LOW)
			GPIO.output(LINKIT_OUT_1, GPIO.LOW)
			if GPIO.input(LINKIT_IN_HOLD)==0:
				state=0

		elif state==2:
			GPIO.output(LED_PIN,GPIO.HIGH)
			GPIO.output(LINKIT_OUT_0, GPIO.LOW)
			GPIO.output(LINKIT_OUT_1, GPIO.LOW)
			if GPIO.input(LINKIT_IN_HOLD)==0 or GPIO.input(LINKIT_IN_STOP)==1:
				state=0
			
			else:
				os.system("python2 play_music.py")
			
		else:
			break

except KeyboardInterrupt:
	GPIO.cleanup()
