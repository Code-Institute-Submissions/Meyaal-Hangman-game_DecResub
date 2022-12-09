import re


class ValidateInput():
    __pattern = "[a-zA-Z]$"

    __ok = "OK"
    __invalid = "Invalid code, please enter again:"

    def __init__(self):
        pass

    def validate(self, value):
        if re.match(self.__pattern, value):
            print(self.__ok)
            return True
        else:
            print(self.__invalid)
            return False
