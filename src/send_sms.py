# Prj: erin-message-bot
# Author: Daniel Gisolfi
# Date: 8.11.17
# send_sms.py

#import all twilio dependencies
from twilio.rest import Client
#import time and random modules
import time, random, datetime
from random import randint
#import module with possible messages
from erinMessages import messages, dayCheck
import os, sys, json
from progress import progress


def reminder():

	#get authentication sid from config vars	
	account_sid = os.getenv('account_sid')
	#get authentication token from config vars
	auth_token = os.getenv('auth_token')
	#chose wich cell phone number from the list to direct the message towards
	my_cell = os.getenv('ENum')
	#get twilio account number from config vars
	my_twilio = os.getenv('my_twilio')

	#run twilio function and pass in authentication info
	client = Client(account_sid,auth_token)

	#create  loop
	while True:
		#uses the datetime library to get the current date
		now = datetime.datetime.now()
		#gets the month
		month = now.month
		#gets the day
		day =  now.day

		#uses the dayCheck function to get the right message else a random one.
		my_msg = dayCheck(month,day)
		
		#send a sms from twilio number to cell with my_msg as text
		message = client.api.account.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
		#print a conformation that the task has completed
		print("Message sent to Erin Gisolfi, Hours until next message:")

		#create a random interval of time between 1 - 8 hours
		waitTime = randint(10800,43200)
		print(waitTime/60/60)
		i = 0
		while i < waitTime:
		    progress(i, waitTime, status='waiting to send next message')
		    time.sleep(0.5)  # emulating long-playing job
		    i += 1
		#print aprox how many hours the function will sleep
		


		#set the fucntion to sleep for x amount of time then run again, and loop
		print("Start : %s" % time.ctime())
		# print("Start")
		time.sleep(waitTime)
		# print("End")
		print("End : %s" % time.ctime())
		

reminder()