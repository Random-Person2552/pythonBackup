from __future__ import print_function # use Python 3.0 printing 
'''Procedure'''
#1-5: Nothing
'''Part 1: Conditionals'''
#6a Prediction: The conditional will return true
#Prediction was right
#6b Prediction: The conditional will return true
#Prediction was correct
#7 Conditional:  40 < x and x < 130 and 100 < y and y < 120
#8
'''Part 2: if else Structures the print Function'''
#9
def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is', AGE_LIMIT)
    
#9a Predictions: 10 is below the age limit and 16 is old enough
'''9a explained: This output occurs because the function checks the inputed age 
against the age limit variable defined, and provide the age is below the limit 
if the age is under 13, like 10, and the age is old enough if the age is above 
13, like 16'''
def report_grade(percent):
    '''Step 9b If-Else'''
    if percent >= 80:
        print('A grade of', percent, 'indicates mastery. Keep up the good work!'  )
    if percent < 80:
        print('A grade of', percent, 'does not indicate mastery. Seek extra practice or get help.')
#10
'''Part 3: The in operator and an introduction to collections'''
#11
def letter_in_word(guess, word):
    '''Returns true if a letter is in a word, otherwise returns false'''
    if guess in word:
        return True
    else:
        return False
#12
def hint(color, secret):
    if color in secret:
        print ("The color " + color + " IS in the secret sequence of colors.")
    else:
        print ("The color " + color + " IS NOT in the secret sequence of colors.")
'''CONCLUSION'''
'''1 Only the blocks of code indented properly will run when the conditional is 
met, otherwise they will not be activated and treated as single lines
#2 There are many operators that can be used to create boolean expressions, such 
as and, or, not, greater than, less than etc. Not in can also be used to create 
boolean expresions
#3a Ira: Ira is not correct, the program only executes that once, so condesining 
it into a single line will still run that line, so the program will not speed up 
or slow down.
#3b Jayla: Jayla is the most correct out of all the arguments, as if you wanted 
to change the print message, you would have to change is twice for each line, 
but by condesing it, you only have to change one line. This is simalr to using 
variables for expressions, as they are easier to change. 
#3c Kendra: Kendra is correct, but removing one line of code will not make a 
large enough different to the storage size of the file for it to be a valid argument. 
'''
'''Assignment Check'''

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)

    