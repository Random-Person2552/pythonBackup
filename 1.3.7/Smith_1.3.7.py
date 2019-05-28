from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

'''Part 1: For loops, range() and help()'''
def days():
    ''' For each letter in the string, prints the letter concatenated to day, 
    then at the end for each number from 5 - 8 not including 8, prints that it 
    is the number day of september
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')
    
#6a
def roll_hundred_pair():
    '''Rolls one hundred pairs of dice and creates a histogram of the results'''
    x = []
    counter = 0
    while counter <= 100:
        counter += 1
        x.append((random.randint(1,6) + random.randint(1,6)))
    plt.hist(x)
    plt.savefig('1.3.7/roll_hundred_pair')
#6b
def dice(n):
    '''Rolls n dice and returns the sum of all of them'''
    x = 0
    for i in range(n):
        x = x + random.randint(1,6)
    print (x)
'''Part 2: While loops'''
#7
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
#Line 2 is necessary because otherwise you could initiate the first guess to a
# letter that is actually in the word.
#8
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Randomly selects a winner from the list of players, allows the user to 
    guess which player one until they get it right, then returns the amount
    of guesses it took.
    '''
    winner = random.choice(players) 

    ####
    # Prints all of the names the user has to guess from
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # Goes from front of list to last 
    #name not including the last name, as the last name does not need the comma 
    #at the end of the print statement
        print(p+', ', end='')
    print(players[len(players)-1]) # Prints the last name without a comma at the end

    ####
    # Adds one to your guess each time you are not able to correctly guess the 
    # winner of the lottery, but if you are, prints that you guessed the winner.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
#9
def goguess():
    '''Picks a random number between 1 and 20 inclusive, user can guess any number 
    between the two, and will be told whether the answer is higher or lower than 
    the guess. If they guess correctly, returns the number of guesses it took.'''
    answer = random.randint(1, 20)
    guess = raw_input("Guess a number between 1 and 20 inclusive. ")
    guess = int(guess)
    attempts = 1
    while guess != answer:
        if guess > answer:
            print (guess, "is too high.")
            guess = raw_input("Guess again. ")
            guess = int(guess)
        elif guess < answer:
            print (guess, "is too low.")
            guess = raw_input("Guess again. ")
            guess = int(guess)
        attempts += 1
    print ("Right, you guessed in", attempts, "attempts.")
#10 To guess between 1 and 6000, you will need at most 13 guesses. Because you
# are given higher and lower each time, you can guess 3000, then 1500, then 750
# 375, 187, 93, 46, 23, 11, 5, 2. At this point there is one answer left if
# it is below 2, and 2 if it is above 2. Since you want the guaranteed, if it is 
# above, you guess 2 more times assuming worst case scenario, leaving you with 13
# guesses.
'''Part 3: Practice'''
#11a
def matches(ticket, winners):
    '''Takes 2 lists, and determines how much of the ticket list matches the winners
    list.'''
    same = 0
    for i in range(len(winners)):
        if ticket[i] in winners:
            same += 1
    return same
#11b
def report(guess, secret):
    '''Takes 2 lists of mastermind colors and returns how many are in the right 
    place and how many are in the wrong place.'''
    right_place = 0
    wrong_place = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            right_place += 1
            secret[i] = 'taken'
        elif guess[i] in secret:
            wrong_place += 1
    print (right_place, "in the right place", wrong_place, "in the wrong place")
'''Conclusion'''
#1 Some of the disadvantages of developing a program this way are that you must 
# type every line, which could lead to having bad code as there are more things
# that could go wrong. With a loop, if you want to change something, it is easier
# than having to change every line in the program.

#2 Using loops to analyze large amounts of data allows you to loop through 
# every value in the data set without having to call each value by hand.

#3 A while loop will continue to iterate everything in the loop until the condition
# it is using is false, where as a for loop will most likely run through a certain
# iteration multiple times using the range() function.

#4 My partner and I worked well together, as we are able to communicate what we 
# need to get done and how to solve a problem. We are also not afraid to ask each
# other for help, allowing us to get work done faster.
'''
Assignment Check
roll_hundred_pair()
dice(10)
dice(20)
goguess()
print (matches([1, 4, 5, 6, 1, 5], [1, 5, 4, 5, 3, 4]))
report(['red', 'red', 'red', 'yellow', 'yellow', 'green'], ['red', 'red', 'yellow', 'yellow', 'green', 'green'])
'''

def super_picks():
    counter = 0
    while counter < 1000:
        picks()
        counter += 1
        
def roll_hundred():
    counter = 0
    while counter < 200:
        roll_hundred_pair()
        counter += 1