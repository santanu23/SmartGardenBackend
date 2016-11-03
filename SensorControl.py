import time
import RPi.GPIO as GPIO



ledPin = 21;#probably not 21
lightThresh = 750
global ledStatus




#switchLEDfuction
def switchLeds(turnOnSignal):
    if(turnOnSignal):
        GPIO.ouput(ledPin,GPIO.LOW)
    else:
        GPIO.ouput(ledPin,GPIO.HIGH)



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

  #      if values[1] < lightThresh :#and on is False:
 #           print("Should be on")
#            switchLeds(True)
#            ledStatus = True
  #      elif values[1] > lightThresh :#and on is True:
  #          print("Should be on, but ambient light is high enough")
    #        switchLeds(False)
#            ledStatus = False
    
#        else:
#        print("Should be off")
#        if on is True:
#            switchLeds(False)

            print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)

