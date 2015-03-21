from .ev3dev import LegoSensor, Motor
import time

#Sensor Init
colorL = ColorSensor(port=0)
colorR = ColorSensor(port=1)
gyro = ColorSensor(port=2)
ultrasonic = ColorSensor(port=3)
USAngle = 0
USDist = 360			#Absolute amount to turn US 360 degrees

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
a.pulses_per_second_sp = 2000
b.pulses_per_second_sp = 2000
c.pulses_per_second_sp = 2000
time.sleep(5)
a.pulses_per_second_sp = 0
b.pulses_per_second_sp = 0
c.pulses_per_second_sp = 0
defaultSpeed = 1000

def calibrateUS():
	turnUS(360)

def turnUS(angle):
c.run_position_limited(100,(angle/360.0)*USDist)
USAngle += angle
if(USAngle < 0)
	USAngle += 360
elif(USAngle > 360)
	USAngle -= 360