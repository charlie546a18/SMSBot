# Prj: erin-message-bot
# Author: Daniel Gisolfi
# Date: 11.20.17
# erinmessages.py

import random

def dayCheck(month,day):
	#if its erin's birthday say happy brithday
	if month == 8 and day == 27:
		my_msg = "Happy Birthday lil ern!"
	else if month == 12 and day == 25:
		my_msg = "MERRY CHRISTMAS!"
	else if month == 11 and day == 23:
		my_msg = "Happy Turkey Day"
	else if month == 1 and day == 1:
		my_msg = "HAPPY NEW YEAR!!! Make it a good one!"
	else if month == 11 and day == 20:
		my_msg = "Dude its today"
	else:
		#pick a random message from 'messages' list
		my_msg = random.choice(messages)

#a list of possible messages that can be sent to users
messages = [
	"Hey erin just gotta remind you you're beautiful",
	"Erin I know you got a lot to do but keep on going lil bud",
	"Fun Fact: ur pretty",
	"Your actions have proved that you are not the type of person who gives up easily.",
	"Your humility is inspiring to those who are watching your success.",
	"I luv ya erin, and so does marty!",
	"I hope you have an awsome day",
	"In the middle of every difficulty lies opportunity.",
	"You look great today!",
	"Your outfit is on point!!!",
	"Hold on, the weekend is almost here.",
	"Today is gonna be a great day!",
	"Remember to treat yo self.",
	"Remember to make every day the best it can be",
	""
]
