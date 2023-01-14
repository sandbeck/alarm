from gpiozero import LED, Buzzer, MotionSensor, Button, OutputDevice
from signal import pause
from time import sleep

lys = LED(4)
sirene = Buzzer(17)
pir = MotionSensor(18)
knap = Button(22, hold_time=2)

# keypad matrix
kol1 = OutputDevice(5)
kol2 = OutputDevice(6)
kol3 = OutputDevice(13)
kol4 = OutputDevice(19)

r1 = Button(20, pull_up=None, active_state=True)
r2 = Button(21, pull_up=None, active_state=True)
r3 = Button(23, pull_up=None, active_state=True)
r4 = Button(24, pull_up=None, active_state=True)
r5 = Button(25, pull_up=None, active_state=True)

def startAlarm(input):
	sleep(0.1)
	if input.value:
		sirene.beep(on_time=0.1, off_time=0.1)
		lys.blink(on_time=0.2, off_time=0.2)
		pir.when_motion = None

def nedtalling():
	sirene.beep(on_time=0.1, off_time=0.9, n=9)
	lys.blink(on_time=0.1, off_time=0.9, n=9)
	sleep(9)
	lys.on()
	sirene.on()
	sleep(1)
	lys.off()
	sirene.off()

def aktiverAlarm(input):
	print("Alarm aktiveret!")
	nedtalling()
	lys.blink(on_time=0.1, off_time=5)
	sirene.off()
	pir.when_motion = startAlarm
	knap.when_pressed = deaktiverAlarm

def deaktiverAlarm():
	pir.when_motion = None
	sirene.off()
	lys.off()

def keypad(input):
	print("knap trykket ned")

knap.when_held = aktiverAlarm

kol1.on()
kol2.on()
kol3.on()
kol4.on()

r1.when_activated = keypad

print('Program startet.')
pause()
