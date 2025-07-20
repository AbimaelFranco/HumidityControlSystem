import RPi.GPIO as GPIO
import time

PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN, GPIO.HIGH)
print("Led encendido")
time.sleep(2)

GPIO.output(PIN, GPIO.LOW)
print("Led apagado")
time.sleep(2)

GPIO.cleanup()