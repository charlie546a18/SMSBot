from src.bot import *
import pytest

class TestBot:        
    # Check whether the function will fail gracefully on 
    # inability to retrieve keys
    def testOSVars_Failure(self):
        var_ids = [
            'NOT',
            'VALID',
            'KEYS'
        ]

        with pytest.raises(SystemExit):
            getOSVars(var_ids)

    # Check wether the types of the returned variables 
    # are of type string
    def testOSVars_Type(self):
        var_ids = [
            'account_sid',
            'auth_token',
            'account_num',
            'target_num'
        ]

        vars = getOSVars(var_ids)
        for var in vars:
            assert type(var) == str

    # Check the getMessage Function
    def testGetMessage(self):
        # Create a Dummy Bot to test functionality
        bot = createFakeBot()

        # Ensure the get message function returns a string
        assert bot.getMessage('src/messages.json')

        # Check that if the file cannot be found an error is thrown
        with pytest.raises(SystemExit):
            bot.getMessage('test_failure.json')
        
        bot.__del__()

    # Check the sendMessage Function
    def testSendMessage(self):
        # Create a Dummy Bot to test functionality
        bot = createFakeBot()
        # Check if the message send failure is handeled
        with pytest.raises(SystemExit):
            bot.sendMessage('TEST MESSAGE')

def createFakeBot():
    bot = Bot(
        'ACXXXXXXXXXXXXXXXXX',
        'YYYYYYYYYYYYYYYYYY',
        '+12316851234',
        '+15555555555', 
        name='FAKE'
    )
    return bot

if __name__ == "__main__":
    tests = TestBot()

