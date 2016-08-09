#! /usr/bin/python
import os
import time
import wakeonlan
from wakeonlan import wol #imports wake on lan from module
from twilio.rest import TwilioRestClient #imports twilio api

#function to send wol magic packet
def powerON():
 wol.send_magic_packet('ff.ff.ff.ff.ff.ff')

#function to send text update via twilio
def phoneUpdate(message):

 #account information for Twilio API
 acccountSID = 'AC0251a9ab7169cc0cc1a0e07030295fcd'
 authToken = 'c857634ea93a5ad0bf098f43ffdf3c93'

 myCellPhone = '+15412211759'
 myTwilioNumber = '+5412142827' 

 twilioCli = TwilioRestClient(accountSID, authToken)
 twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)

#function to ping phone and pc and check response
def wifiScan():
 hostname1 = "gingipc" #example
 hostname2 = "gingiphone"
 response = os.system("ping -c 1 " + hostname1)
 response2 = os.system("ping -c 1 " + hostname2)


 #and then check the response...
 if response == 0:
  print hostname1, 'is up!'

 else:
  print hostname1, 'is down!'

 if response2 == 0:
  print hostname2, 'is up'
  return True

 else:
  print hostname2, 'is down'
  return False

#stops the script for 30 seconds
 time.sleep(30)

if wifiScan() == True:
 print 'power on'
 powerON()

#make this not endless loop
#while True:
#	wifiScan()


