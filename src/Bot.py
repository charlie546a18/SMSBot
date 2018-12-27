# !/usr/bin/python3
# Version 2.0

#import all twilio dependencies
from twilio.rest import Client
import datetime
import holidays
import random
import json
import sys
import os

class Bot:
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.account_sid = args[0]
        self.auth_token = args[1]
        self.account_num = args[2]
        self.target_num = args[3]
        self.enabled = True
        print(f'Bot: {self.name} created')

    def __repr__(self): 
        return f'Object: {self.string}'
        
    def sendMessage(self, msg):
        # Declare the Client with the Bots API Info
	    client = Client(self.account_sid, self.auth_token)

        # Send a sms from twilio number to cell with my_msg as text
        message = client.messages.create(
            to=self.target_num, 
            from_=self.account_num, 
            body=msg
        )

		# result = client.api.account.messages.create(to=self.target_num, from_=self.account_num, body=msg)
        print(message.sid)
    def getMessage(self):
        file = open('messages.json')
        messages = file.read()
        json_data = json.loads(messages)
        random.choice(json_data['messages'])

    def checkForHoliday(self, date):
        us_holidays = holidays.US()
        return us_holidays.get(date)

    def checkDate(self):
        d = datetime.datetime.today()
        date = d.strftime('%Y-%m-%d')
        year_month = d.strftime('%m-%d')
        holiday = self.checkForHoliday(date)
        if holiday != None:
            if holiday == 'Christmas Day':
                return 'Merry Christmas!'
            elif holiday == "New Year's Day":
                return 'Happy New Year!'
            elif d.year_month == '12-23':
                return 'Merry Eve of Christmas Eve!'
            elif d.year_month == '12-24':
                return 'Merry Christmas Eve!'
            elif d.weekday() == 5:
                return 'The Weekend is almost here!!!'
            else:
                return f'Have a Great {holiday}'
        return None

    def loop(self):
        try:
            while self.enabled:
                # Check the Day
                message = self.checkDate()
                # Get the Message to be sent
                if message == None:
                    message = self.getMessage()

                # Send the Message
                self.sendMessage(message)

                # Get a random interval of time to wait for
                # Once waiting has finished Send another message
                
        except KeyboardInterrupt:
            print('Bot Interupted')

    def progess(self):
        pass

    def __del__(self):
        print(f'Deleted Bot: {self.name}')


def getOSVars(var_ids):
    values = []
    for var_id in var_ids:
        try:  
            values.append(os.environ[f'{var_id}'])
        except KeyError: 
            print(f'Enviorment Variable: {var_id} was not set')
            sys.exit(1)
    return values


if __name__ == "__main__":
    var_ids = [
        'account_sid',
        'auth_token',
        'account_num',
        'target_num'
    ]

    vars = getOSVars(var_ids)
   
    bot = Bot(
        vars[0],
        vars[1],
        vars[2],
        vars[3],
        name='Marty'
    )

    bot.loop()



