'''
efficiency.py defines two algorithms that each decide whether a number is prime.
The __main__ code times the algorithms.

version 2/21/2014
Unpublished work (c) 2014 Project Lead The Way, Inc.
'''

import random
import timeit

def is_prime_versionA(number):
    """ Returns True if number is prime.
    Returns False otherwise.
    """
    # Refuse a very long execution time
    if number > 2**30: # # 2**30 is about 7.2e16, which means 72,000,000,000,000,000
        return "That number is too big to run this algorithm quickly."
    
    # Refuse anything but positive integers
    if type(number) != int or number<1:
        return "That number is not a positive integer."
        
    # Initialize a one-way flag 
    prime = True
    
    # Check all possible divisors 
    # from 2 to number-1
    for possible_divisor in range(2, number-1):
        if number % possible_divisor == 0: 
            # No remainder, so it's a factor
            prime = False 

    return prime
    
def is_prime_versionB(number):
    """ Returns True if number is prime.
    Returns False otherwise.
    """
    # Refuse a very long execution time
    if number > 2**30: # # 2**30 is about 7.2e16, which means 72,000,000,000,000,000
        return "That number is too big to run this algorithm quickly."
    
    # Refuse anything but positive integers
    if type(number) not in (int, long) or number<1:
        return "That number is not a positive integer."
        
    # Check is number is even
    if number%2 == 0:
        return False
        
    # If there are divisor pairs, 
    # one divisor is <= number's square root
    max_divisor = int(number**0.5)
    max_divisor += 1 # So that range includes the square root
    # Check all possible divisors
    # from the odd numbers
    for possible_divisor in range(3, max_divisor, 2):
        if number % possible_divisor == 0: 
            # No remainder, so it's a factor
            return False 

    return True
           
####
# main function  
####

# The if __name__ == "__main__": condition is commonly used 
# to enclose code in a Python file that is outside a function, i.e. procedural programming. 
# It allows this file to be imported by other code without having the 
# following code executed by that file's import statement.
# We are introducing it here because timeit also will need to refer to __main__
# and for a student it might be nicer to see the more common use of __main__

if __name__ == "__main__": 
    '''Time the two options
    '''
    n_trials=8
    n_executions=10000
    print "I will check whether a number is prime using each of two algorithms."
    print "I will run each algorithm 80,000 times and report "
    print "the time for each set of 10,000 executions."
    print
    number = int(raw_input("What number would you like me to check? "))
    
    # Refuse a very long execution time.
    if number > 5000: #
        print number, " is too large to factor in a reasonable amount of time."
    else:
        print "Testing execution time to decide whether", number, "is prime"
        # Create two Timer objects that each time a particular statement
        clock1 = timeit.Timer(stmt="is_prime_versionA(number)", 
                              setup="from __main__ import number, is_prime_versionA")
        clock2 = timeit.Timer(stmt="is_prime_versionB(number)", 
                              setup="from __main__ import number, is_prime_versionB")
        # The <from __main__ import variables and functions> is
        # needed because timeit statements have to be self-contained;
        # they can't use functions and variables from other code in this file 
        # unless they import them.
                                      
        # Measure n_trials groups of n_executions for algorithm 1
        print 
        for i in range(n_trials):
            # The timeit method of a Timer object 
            # executes the Timer's setup, 
            # starts a stopwatch, 
            # executes the Timer's statement n_executions times, 
            # and stops the stopwatch
            this_time = clock1.timeit(n_executions)
        
            # Output the time for each batch of executions
            print this_time, "seconds for ", n_executions, " executions of is_prime_versionA(", number, ")."

        print
        # Measure n_trials groups of n_executions for algorithm 2
        for i in range(n_trials):
            # The timeit method of a Timer object 
            # executes the Timer's setup, 
            # starts a stopwatch, 
            # executes the Timer's statement n_executions times, 
            # and stops the stopwatch
            this_time = clock2.timeit(n_executions)
        
            # Output the time for each batch of executions
            print this_time, "seconds for ", n_executions, " executions of is_prime_versionB(", number, ")."
        
        print
