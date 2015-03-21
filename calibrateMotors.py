from ev3.lego import LegoSensor, Motor, ColorSensor
import time

#Sensor Init
colorL = ColorSensor(port=1)
colorR = ColorSensor(port=2)
gyro = ColorSensor(port=3)
ultrasonic = ColorSensor(port=4)
USAngle = 0
USDist = 2515			#Absolute amount to turn US 360 degrees

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
c.pulses_per_second_sp = 0
defaultSpeed = 1000
a.stop()
b.stop()
c.stop()

def calibrateMotors():
	driveForwardDist(500,335)

def driveForwardDist(speed, dist):
	a.run_position_limited(dist, speed)
	b.run_position_limited(dist, speed * 1.2)

calibrateMotors()