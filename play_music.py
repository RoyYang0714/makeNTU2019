import pygame
import RPi.GPIO as GPIO

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

GPIO.setup(LINKIT_IN_HOLD, GPIO.IN)
GPIO.setup(LINKIT_IN_STOP, GPIO.IN)
GPIO.setup(LINKIT_IN_MUS_1, GPIO.IN)
GPIO.setup(LINKIT_IN_MUS_2, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LINKIT_OUT_0, GPIO.OUT)
GPIO.setup(LINKIT_OUT_1, GPIO.OUT)


GPIO.output(LED_PIN, GPIO.HIGH)
GPIO.output(LINKIT_OUT_0, GPIO.LOW)
GPIO.output(LINKIT_OUT_1, GPIO.LOW)

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	if GPIO.input(LINKIT_IN_HOLD)==0 or GPIO.input(LINKIT_IN_STOP)==1:
		pygame.mixer.music.stop()
		break

	elif GPIO.input(LINKIT_IN_MUS_1)==0 and GPIO.input(LINKIT_IN_MUS_2)==0:
		pygame.mixer.music.set_volume(0.2)

	elif GPIO.input(LINKIT_IN_MUS_1)==0 and GPIO.input(LINKIT_IN_MUS_2)==1:
		pygame.mixer.music.set_volume(0.45)

	elif GPIO.input(LINKIT_IN_MUS_1)==1 and GPIO.input(LINKIT_IN_MUS_2)==0:
		pygame.mixer.music.set_volume(0.7)

	elif GPIO.input(LINKIT_IN_MUS_1)==1 or GPIO.input(LINKIT_IN_MUS_2)==1:
		pygame.mixer.music.set_volume(1)