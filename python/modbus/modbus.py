from minimalmodbus import Instrument

import RPi.GPIO as GPIO

RS485_DIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(RS485_DIR_PIN, GPIO.OUT)

def switch(instrument, is_write):
    instrument.serial.flush()

    if is_write == True:
        GPIO.output(RS485_DIR_PIN, GPIO.HIGH)
    else:
        GPIO.output(RS485_DIR_PIN, GPIO.LOW)

instrument = Instrument('/dev/serial0', 0x21, before_transfer=switch)

instrument.serial.baudrate = 115200
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 0.2           # seconds
instrument.mode = minimalmodbus.MODE_RTU   # RTU or ASCII mode
instrument.clear_buffers_before_each_transaction = True

try:
    print("CMD counter: %d" % instrument.read_register(0x8000))
except IOError:
    print("Failed to read from instrument")
