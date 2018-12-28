from src import bot
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
            bot.getOSVars(var_ids)

    # Check wether the types of the returned variables 
    # are of type string
    def testOSVars_Type(self):
        var_ids = [
            'account_sid',
            'auth_token',
            'account_num',
            'target_num'
        ]

        vars = bot.getOSVars(var_ids)
        for var in vars:
            assert type(var) == str

    # 
    def testGetMessage(self):
        # Ensure the get message function returns a string
        assert bot.getMessage('messages.json')

        # Chek that if the file cannot be found an error is thrown
        with pytest.raises(SystemExit):
            bot.getMessage('test_failure.json')

if __name__ == "__main__":
    tests = TestBot()

