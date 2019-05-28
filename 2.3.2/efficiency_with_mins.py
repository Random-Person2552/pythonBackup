'''
efficiency_with_mins.py defines two algorithms that each decide whether a number
is prime. The __main__ code times the algorithms and reports minimum times.

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
    if number > 2**26: # # 2**26 is about 67,000,000
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
    if number > 2**60: # # 2**30 is about 7.2e16, which means 72,000,000,000,000,000
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
    max_divisor += 1 # So range() includes it
    
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
    number = int(float(raw_input("What number would you like me to check? (enter 0 to quit) ")))
    
    while number != 0:
        print "Testing execution time to decide whether", number, "is prime"
        # Create two Timer objects that each time a particular statement
        print "Minimum time for ", n_executions, " executions of is_prime(", number, "):"
        print "     Data:",number,"     VersionA:", 
        
        # Refuse a very long execution time or run algorithmA and print result.
        if number > 5000:
            print "too slow; not measured",
        else:
            # Create a time object
            clock1 = timeit.Timer(stmt="is_prime_versionA(number)", 
                        setup="from __main__ import number, is_prime_versionA")
            # Initialize an aggregator
            timesA = [] 
            for i in range(n_trials):
                # Measure n_trials groups of n_executions
                this_timeA = clock1.timeit(n_executions)
                timesA.append(this_timeA)
            print min(timesA),
                
        # Measure n_trials groups of n_executions for algorithmB and print result
        timesB = []
        clock2 = timeit.Timer(stmt="is_prime_versionB(number)", 
                    setup="from __main__ import number, is_prime_versionB")
        for i in range(n_trials):
            this_timeB = clock2.timeit(n_executions)
            # Aggregate the times for later selection of the minimum
            timesB.append(this_timeB)
        # Output the minimum time for each batch of executions
        print "     VersionB:", min(timesB)
        print
        number = int(float(raw_input("What number would you like me to check? (enter 0 to quit) ")))
