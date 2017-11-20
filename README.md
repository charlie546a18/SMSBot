# Erin-Message-Bot

This is a minnimal one way(for now) chat bot. It sends outgoing text-messages to whoever the contacts list is set as.

### Prerequisites

All requiremnets to run a instance of this project

* Twilio API
* Heroku CLI

## Deployment

Currently I have a version of this running on a Heroku web server to run your own instance you can use any  simmilar web service.

## Basic Understanding

This is a very simple web bot that uses the following code found on the [Twilio](https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest) site to send messages to a user.

```python
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12316851234",
    from_="+15555555555",
    body="Hello there!")
```



##Built With

[Twilio](https://github.com/twilio) - An API used to send and receive text messages.

## Author

- **Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://gist.github.com/PurpleBooth/LICENSE.md) file for details

## Acknowledgments

- Twilio API - this bot leans heavily on twilio's API
- Inspiration - My sister requested i create her an inspirational bot, here is the basic version of it