from ev3.lego import LegoSensor, Motor, ColorSensor
import time

#Sensor Init
colorL = ColorSensor(port=1)
colorR = ColorSensor(port=2)
gyro = ColorSensor(port=3)
ultrasonic = ColorSensor(port=4)
USAngle = 0
USDist = 2515		#Absolute amount to turn US 360 degrees

#MotorInit
def init_motor(motor):
	print ("Initializing motor")
	motor.reset()
	motor.run_mode = 'forever'
	motor.stop_mode = Motor.STOP_MODE.BRAKE
	motor.regulation_mode = True
	motor.pulses_per_second_sp = 0
	motor.start()
	print ("Motor Initialized")
	return;

a = Motor(port=Motor.PORT.A)
b = Motor(port=Motor.PORT.B)
c = Motor(port=Motor.PORT.C)
init_motor(a)
init_motor(b)
init_motor(c)
#a.pulses_per_second_sp = 2000
#b.pulses_per_second_sp = 2000
#c.pulses_per_second_sp = 2000
#time.sleep(5)
a.pulses_per_second_sp = 0
b.pulses_per_second_sp = 0
c.pulses_per_second_sp = 2000
defaultSpeed = 1000
a.stop()
b.stop()
c.stop()

def calibrateUS():
	turnUS(360)

def turnUS(angle):
	c.run_position_limited((angle/360.0)*USDist,1000)
	global USAngle
	USAngle += angle
	if(USAngle < 0):
		USAngle += 360
	elif(USAngle > 360):
		USAngle -= 360

calibrateUS()