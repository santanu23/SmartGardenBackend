import time
import RPi.GPIO as GPIO



ledPin = 21;
pumpPin = 16;# may change it later
lightThresh = 750
global ledStatus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pumpPin,GPIO.OUT)


#switchLEDfuction
def switchLeds(turnOnSignal):
    if(turnOnSignal):
        GPIO.ouput(ledPin,GPIO.HIGH)
    else:
        GPIO.ouput(ledPin,GPIO.LOW)

##Time to start the light in the morning
startH = 9
startM = 0

##Time the light should be turned of in the evening
stopH = 17
stopM = 57

##Save the last time a pump was active
##Having a minimum time between pump cycles ensures that the soil has enough time to absorb the water
##and the moisture sensor can read the new values. Decreasing the time between pump cycles increases the danger of pumping too much water
lastPumpTime = [time.time(),time.time()]
minTimeBetweenPumps = 30

def switchPump(pump):
    
    timeDelta = time.time() - lastPumpTime[pump]
    
    if timeDelta > minTimeBetweenPumps:
        GPIO.output(pumpPin, GPIO.LOW)
        time.sleep(pumpTime)
        GPIO.output(pumpPin, GPIO.HIGH)
        lastPumpTime[pump] = time.time()
##############################################################
print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| vegTro1 | Lights | waterLev | vegTro2 |'.format(*range(4)))
print('-' * 37)

# Main loop.
while True:
    
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
        if(values[0] >800):
            print('the value is ')
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)
##############################################################


def centralControl():
while True:
    lightReading = readLight()
    veg1 = readVegOne()
    veg2 = readVegTwo()
    waterLev = readWaterLev()

if (t.hour > startH or (t.hour == startH and t.minute >= startM)) and (t.hour < stopH or (t.hour == stopH and t.minute < stopM)):
    if lightReading < lightThresh and on is False:
        print("Should be on")
            switchLeds(True)
        elif light > lightThresh and on is True:
            print("Should be on, but ambient light is high enough")
            switchLeds(False)

else:
    print("Should be off")
        if on is True:
            switchLeds(False)


for i in range (0, len(moisture)):
    if moisture[i] < moistureThresh[i]:
        switchPump(i)
    
    time.sleep(2)



