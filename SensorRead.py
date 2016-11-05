# Import the ADS1x15 module.
import Adafruit_ADS1x15
import smbus
import time

#############################vegT sensor method#############################################
adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1

##############################################################
print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| vegTro1 | Lights | waterLev | vegTro2 |'.format(*range(4)))
print('-' * 37)


##############################################################


###############################################################3

def readVegOne():
    # Read the specified ADC channel using the previously set gain value.
    vegOneReading = adc.read_adc(1, gain=GAIN)
    return vegOneReading

def readVegTwo():
    # Read the specified ADC channel using the previously set gain value.
    vegTwoReading = adc.read_adc(3, gain=GAIN)
    return vegTwoReading

def readWaterLev():
    # Read the specified ADC channel using the previously set gain value.
    waterLevReading = adc.read_adc(2, gain=GAIN)
    return waterLevReading

#############################Light sensor method#############################################

DEVICE     = 0x23 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
    # Simple function to convert 2 bytes of data
    # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)

###############################
