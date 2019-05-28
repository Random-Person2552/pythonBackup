import random
'''Part 1: Tuples, Syntax'''
#4 (3, 6, 7)

#5 In math, when we turn in our homework, we have to staple it to our notes and
# turn in both. Our teacher wants us to be descriptive in our variable names
# so that we know what each variable does, but does not have a specific naming
# convention.

#6a will result in 'b' being printed because it is the 2nd value

#6b will print 'a' , 'b', as it does not include the last index given. 
# This selects from the beginning to the 2nd index, not including the 2nd index

#7a will result in true, as since tuples cannot change, so the second value is 
# still 10.

#7b will result in 15, as you reiterate the tuple after a has changed, so the
# second value also changes

'''Part 2: Lists'''
#8 'b', 3 , as the selectors select from the 1st index, including the first index
# to the end

#9 False, as values[2] has been reassigned to a string, not an integer

#10a values will return ['a', 'b', '3', 4, 5], as when you concatenate lists,
# the lists combine into one list.

#10b will return ['a', 'b', '3', 4, 5, [6, 7]], as you are appending a list to 
# a  list, so the list goes at the end of the other list, giving you a list
# inside of a list

#11 This is the same as trying to concatenate a string and an integer, and as the 

#12  Using *= is the same as using the longhand of taking the value and setting it
# equal to itself times 3, so you are able to use this on the variable to save 
# typing and space

'''Part 3: Lists and the random module'''
def roll_two_dice():
    '''Rolls 2 dice and adds the values'''
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print roll1 + roll2

'''Conclusion'''
#1 A is a string, and can be added to another string and is immutable, B is a tuple 
# and can be added to other things, but is also immutable. C is a list, and can
# be added to another list, but is mutable, as you can change the values at given
# indexes. 

#2 Variable types allow you to change something easily, or carry over a value 
# from another function. You cannot represent everything with an integer
# as with python, to do specific math you have to change one number to a float, 
# so that you get a decimal instead of an integer. The other reason is because 
# of strings, and strings are not able to be stored as an integer, since letters 
# are not numbers

#3
#1.3.2 we learned what the different data types that python used were, and how
# we could use them

#1.3.3 we learned how to use conditionals and boolean operators, and the structure
# of if-else statements

#1.3.4 we learned about glass box testing and test-driven design, and how to 
# create a test function for a function that we have written. We also learned how
# to use the raw_input and type casting, so that we could ask a user for an input

#1.3.5 We learned more about strings, including technicalities for concatenation
# and how we can modify strings or select slices of strings.

#1.3.6 We learned about tuples, and how they cannot be changed once they are created
# and how you cannot reassign values in a tuple, but you can in a list. 

#1.3.6 Function Test
print(roll_two_dice())