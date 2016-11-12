import SensorRead 
import time
import httplib, urllib

# API URL: https://thingspeak.com/channels/179370
apiWriteKey = 'YRREW6MQXXUEKJG3'
apiReadKey = '43JJR329XJJ5WU5I'
apiChannelKey = '130XDIIHOZ65W7Q6'

# Main loop.
while True:
    lightReading = SensorRead.readLight()
    veg1 = SensorRead.readVegOne()
    veg2 = SensorRead.readVegTwo()
    waterLev = SensorRead.readWaterLev()
    params = urllib.urlencode({'field1': lightReading, 'field2': veg1,'field3': veg2,'field4': waterLev,'key': apiWriteKey})     # use your API key generated in the thingspeak channels for the value of 'key'
                        # temp is the data you will be sending to the thingspeak channel for plotting the graph. You can add more than one channel and plot more graphs
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = lightReading
        conn.close()
    except:
        print "connection failed"
    
time.sleep(0.5)
