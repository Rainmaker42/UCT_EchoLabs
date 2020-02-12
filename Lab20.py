'''
lab 20 testing functions

'''

def returnValueTimesValue(value):
    ''' Returns value ** value '''
    value **= value
    return value


userInput = input("The function argument is ")

userInput = int(returnValueTimesValue(float(userInput)))
print("The output of the function is {}".format(userInput))
