'''Procedure'''
#5 The data types int, float and long can store the number 6 million
#6 The second type() function will produce an error, as it cannot concatenate
# a string and an integer
#7 When given a negative input to the index, the machine counts from the back, 
# with the last number becoming 0. 
#8
slogan = 'My school is the best'
print slogan[17:21]
#9
print slogan[:13] + 'awesome!'
print slogan[:13] + 'fun!'
#10a will return 7, as the length of theater is 7 characters
#10b will return 'theate' as you slice from the beginning of the word
# to the length of the word, which would be the end, but minus 1.
#11 In searches for the first input given in the second input given, in this case
# two strings, and returns true if it is able to find the inputs.
#12
def how_eligible(essay):
    counter = 0
    if "?" in essay:
        counter += 1
    if "," in essay:
        counter += 1
    if '"' in essay:
        counter += 1
    if "!" in essay:
        counter += 1
    return counter
        
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

#As a result, you recieve 4 and 1. We know that we have completed the assignment
# as these are the results that occur in the example. 