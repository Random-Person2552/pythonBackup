from __future__ import print_function # must be first in file 
import random

'''Part 1: Nested if structures and testing'''
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
#1a The result was returned from line 17
'''1b Running food_id('orange') will return the result from line 15 
The inputs food_id('orange', 'apple' or 'banana') will return line 17.
The inputs food_id('potato') will return the result from line 20
Any other input will return the result from line 22'''
'''1c Banana will never return starchy because it satisfies a prior if statement,
and when one is satisfied any others below it will not be ran. '''
#2
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
#3
def f(n):
    '''Determines if a given number, n, is an integer, even, odd, or a multiple
    of 6'''
    if type(n) == int:
        if n % 2 == 0:
            if n % 3 == 0:
                return "%s is a multiple of 6" % (n)
            else:
                return "%s is even" % (n)
        else:
            return "%s is not even" % (n)
    else:
        return "%s is not an integer." % (n)
#4
'''You could use a float, like 1.0, an even number that is a multiple of 6, an
odd number, and an even number that is not a multiple of 6. '''
#5
def f_test():
    '''Test suite for prior function, f(n)'''
    test = True
    if f(1.0) != "1.0 is not an integer.":
       test = 'Bug when determining if n is an integer'
    elif f(2) != '2 is even':
       test = 'Bug when determining if number is even'
    elif f(12) !=  '12 is a multiple of 6':
        test = 'Bug when determining if number is a multiple of 6'
    elif f(3) != '3 is not even':
        test = "Bug when determining if number is odd"
    
    if test == True:
        print ("No bugs in code.")
    else:
        print ("Bugs in code")
        print (test)
        
'''Part 2  The raw_input() function, type casting, and print() from Python 3'''
#8
def guess_once():
    '''Picks a random number between 1 and 4 inclusive, then asks you to guess
    the number in one try, and determines if you were too low, high or guessed right'''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess > secret:
            print('Too high - my number was ', secret, '!', sep='')
        else:
            print('Too low - my number was ', secret, '!', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
'''8a line 11 takes 2 strings and a keyword value pair, being print(s1, s2, end=/'!\n/')
the end keyword value pair ends the print function with a new line after the strings
print.'''
#9 
def quiz_decimal(low, high):
    '''Asks you to pick a number between two arguments, a low number and a high 
    number, after which it tells you if you are right or wrong'''
    print('Pick a number between', low, 'and', high, ':')
    guess = float(raw_input())
    if guess > high:
        print('No,', guess, 'is greater than', high)
    elif guess < low:
        print('No,', guess, 'is lower than', low)
    elif guess == high:
        print('No,', guess, 'is equal to', high)
    elif guess == low:
        print('No,', guess, 'is equal to', low)
    else:
        print('Good!', low, '<', guess, '<', high)
'''Conclusion'''
'''1 Glass box testing is when you build a function to check every if statement, 
even ones that will not typically get ran

2 Blocks of code will only run if the condition before them is met, so when one 
if is true, the code under it will run, but if it is false, the code will not run

3 A test suite runs through every part of a function to check that there are no 
bugs. Programmers often write this first because it allows them to see where the 
program will go, then while they are writing the function they can constantly 
check it for bugs

4 Yes, you could create a function for each ouput case'''
def f_integer(n):
    '''Determines if n is an interger'''
    if type(n) == int:
        return '%s is an integer' % (n)
    else:
        return '%s is not an integer' % (n)
        
def f_odd(n):
    '''Determines if n is odd'''
    if n % 2 == 1:
        return '%s is odd' % (n)
    else:
        return '%s is not odd' % (n)
        
def f_even(n):
    '''Determines if n is even'''
    if n % 2 == 0:
        return '%s is even' % (n)
    else:
        return '%s is not even' % (n)
        
def f_multiple(n):
    '''Determines if n is a multiple of 6'''
    if n % 3 == 0 and n % 2 == 0:
        return "%s is a multiple of 6" % (n)
    else:
        return "%s is not a multiple of 6" % (n)
        
'''Challenge'''
def f_challenge(n):
    '''Challenge function using the 4 prior functions'''
    print (f_integer(n))
    print (f_even(n))
    print (f_odd(n))
    print (f_multiple(n))
    
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)
