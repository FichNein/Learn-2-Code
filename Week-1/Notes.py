
# The current file that we are looking at is a python code file
# Its really just a big ol text file, but we call it something special so it feels better about itself

# There are `#` at the start of each line, because these are technically 'comments' in this code file

"""
Comments can also be done in bulk by using three quotation marks. 
Comments are used very often in code to explain what you code is doing. 
They aren't always necessary, but they do often help!
"""


# --------------------------------------------------------------------------------



# Click the arrow in the top right to run it
# Alternatively, use the terminal below and type "python HelloWorld.py"






print("Hello, World!")





"""
If that worked, you should see "Hello, World!" printed down below.
Feel free to change what is inside the quotes, and you'll see the text that prints out changes
Congrats! You are coding :sunglasses:

To move forward, check out the next file `variables.py`
"""


# --------------------------------------------------------------------------------



# Creating Variables

anInteger = 2
anotherInteger = 6

aString = "We put strings inside of quotes"
anotherString = 'we can also put them inside of single quotes, instead of double quotes'
aWord = 'word'

aFloat = 2.51
anotherFloat = 7.0



# What can we do with variables? Print them!

print(anInteger)

print(aString)

print(aFloat)



# Math

totalInteger = anInteger + anotherInteger   # 8
alsoThisOne = anInteger + 14                # 16

totalFloat = aFloat + anotherFloat          # 9.51
alsoFloat = aFloat + 4.4                    # 6.91

addIntAndFloat = anInteger + aFloat         # 4.51

aNumber = 6 + 4.3                           # 10.3


# We can even add strings!

firstHalf = "I have a rabbit. "
secondHalf = "His name is Donovan!"

totalWord = firstHalf + secondHalf

print(totalWord)








# --------------------------------------------------------------------------------








# Create variables
firstNumber = 15
secondNumber = 32

# Do the math
result = firstNumber + secondNumber
resultTimesTwo = result * 2

# Show the result

print(result)
print(resultTimesTwo)








# --------------------------------------------------------------------------------


userName = input("Hello, what is your name? ")
print("Hello " + userName + "!")



userAgeAsString = input("How old are you " + userName + "?")
userAge = int(userAgeAsString)
userAgeInDays = userAge * 365


print("If you are " + str(userAge) + " years old, that means you are about " + userAgeInDays + " days old!")



#---------------------------------------


numFriends = int(input("How many friends? "))
totalBill = int(input("What is the total bill? "))

tip = int(input("What percentage are you tipping? ")) * 0.01

totalAfterTip = totalBill * (1 + tip)

totalPerPerson = totalAfterTip / numFriends

print("Each friend should pay $" + str(totalAfterTip))