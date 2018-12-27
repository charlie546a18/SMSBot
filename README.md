# SMS Bot

This is a minimal one way(for now) chatbot. It sends outgoing SMS to whoever the bot's `target_num` variable is set to.

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Deployment

The SMS Bot is currently deployed in a Docker Container on my personal VM. To deploy another instance of the Bot you can do the following:

1. Get a Twilio SID and Authentication Token as well as an account phone number(do this by creating a new account)

2. Edit the Dockerfile found in the root of the repository to add environment variables. The Bot requires 4, the following is a working example

   ```dockerfile
   # After The intial From Command
   # SET ALL ENVIORMENT VARIABLES
   ENV account_sid=ACXXXXXXXXXXXXXXXXX
   ENV auth_token=YYYYYYYYYYYYYYYYYY
   ENV account_num=+12316851234
   ENV target_num=+15555555555 
   # Before the final run command
   ```

3. Create Image of the edited Dockerfile by running the necessary make command `make build`

   *Note: You can change the name of the bot before running this command in the Bot.py file*

4. The Bot can now be run by using the make command `make all`

## Developing

To make changes or even develop the Bot further a development environment can be created. Simply run `make dev`. When completed change directory to the root of the container and enter the `/DEV` directory. Once inside all files inside the directory are volume mounted for testing purposes.

## Resources

This Bot only has a handful of dependencies(listed in the `requirements.txt` file) however the most important is Twilio. Below is a very simple example of how to send SMS using the Twilio API in python. This example and many more can be found at [Twilio](https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest).

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
