from serial import Serial
from time import sleep
import pyTMCL

# serial-address as set on the TMCM module.
MODULE_ADDRESS = 0

# Open the serial port presented by your rs485 adapter
serial_port = Serial("COM4")

# Create a Bus instance using the open serial port
bus = pyTMCL.connect(serial_port)

# Get the motor
motor = bus.get_motor(MODULE_ADDRESS)
motor.axis.max_positioning_speed = 200
# From this point you can start issuing TMCL commands
# to the motor as per the TMCL docs. This example will
# rotate the motor left at a speed of 1234 for 2 seconds


def angle_to_steps(angle):
    return int(angle * 256 / 1.8)

def callback(arg1, arg2):
	print("Argument 1: " + str(arg1) + "  Argument2: " + str(arg2))

motor.move_relative(angle_to_steps(360), callback=callback, args=("Finished Moving", "Turned 360 Degree"))
