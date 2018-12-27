# Prj: erin-message-bot
# Author: Daniel Gisolfi
# Date: 11.20.17
# erinmessages.py

import random

def dayCheck(month,day):
	#if its erin's birthday say happy brithday
	if month == 8 and day == 27:
		return "Happy Birthday lil ern!"
	elif month == 12 and day == 25:
		return "MERRY CHRISTMAS!"
	elif month == 11 and day == 23:
		return "Happy Turkey Day"
	elif month == 1 and day == 1:
		return "HAPPY NEW YEAR!!! Make it a good one!"
	else:
		#pick a random message from 'messages' list
		return random.choice(messages)

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
	"Whatever you are, be a good one.",
	"If not us, who? If not now, when?",
	"Remember no one can make you feel inferior without your consent.",
	"Wherever you go, go with all your heart.",
	"Do one thing every day that scares you.",
	"You must do the thing you think you cannot do.",
	"Eighty percent of success is showing up, the other 20 percent is doing the the thing but dont worry about that rn"
]
