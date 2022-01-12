#Dominic Enriquez, Martin Bernard
#Textbook: What Can Be Computed?


#Component 2
#Exercise 2.2a
def sum_of_seconds(inputString):
    numbers = inputString.split(' ')
    length = len(numbers)
    sum = 0
    for i in range(1, length, 2):
        sum += numbers[i]
    return str(sum)

#Exercise 2.2b
def sum_of_thirds(inputString):
    numbers = inputString.split(' ')
    length = len(numbers)
    sum = 0
    for i in range(2, length, 3):
        sum += numbers[i]
    return str(sum)

#Exercise 2.2c
def second_sum_is_greater(inputString):
    if sum_of_thirds(inputString) > sum_of_seconds(inputString):
        return 'yes'
    else:
        return 'no'

#Exercise 2.3
def number_of_gs(inputString1, inputString2):
    g1 = 0
    for chr in inputString1:
        if chr == 'G':
            g1 += 1
    g2 = 0
    for chr in inputString2:
        if chr == 'G':
            g2 += 1
    return str(g1) + '\n' + str(g2)

#Component 3
#Exercise 2.4
    #a, d

#Exercise 2.5
    #a: P(I) = 'g'
    #b: P(I) = '435'
    #c: P(I) = undefined
    #d: P(I) = 'defg'
    #e: P(I) = undefined
    #f: P(I) = '11'
    #g: P(I) = '28'
    #h: P(I) = undefined
    #i: P(I) = 'cz'


#Exercise 2.6
    #P and Q are equivalent Python programs

#Exercise 2.7
    #a: This program accepts positive multiples of 10
    #b: This program rejects all other strings that are exclusively made up of ASCII digits
    #c: Strings that include non-digit ASCII characters are neither accepted nor rejected, but rather throw an error
    #d: This program is not a decision program because it does not produce an output for every possible input.


#Component 4
def m(s): return 'no'

#Component 5
    #a: Assume there is a positive integer S such that there are no integers that come after it. 
    # By basic arithmetic, we know there exists an integer R such that R = S + 1. 
    # Thus a contradiction has arisen, and it has been shown that S is not the final positive integer.
    
    #b: Assume there is a negative integer S such that there are no integers that come before it. 
    # By basic arithmetic, we know there exists an integer R such that R = S - 1. 
    # Thus a contradiction has arisen, and it has been shown that S is not the final negative integer.

    #c: Assume there is an even integer S such that there are no even integers that come after it. 
    # By basic arithmetic, we know there exists an integer R such that R = S + 2. 
    # Thus a contradiction has arisen, and it has been shown that S is not the final even integer.

    #d: Assume there is a positive real number S such that there is no positive real number smaller than it
    # By basic arithmetic, we know there exists a positive real number R such that R = S / 2. 
    # Thus a contradiction has arisen, and it has been shown that S is not the smallest.

#Component 6

#Exercise 3.2
#a: P = "def countChars(inputString): return len(inputString)"
#b: 52
#c: P = "def countCharsB(inputString): return len(inputString)     ". 58
#d: The outputs of countChars.py and countCharsB.py are different because 
# the program counts all characters and whitespaces in the program. So, if you
# have extra whitespaces in the program, such as countCharsB.py, then when 
# you pass the program into itself, the whitespaces will be counted as a characters
# in the input. 
    

#Exercise 3.3
def containsGA_GA(inputString):
    string_to_check = 'G' + 'A' + 'G' + 'A'
    if string_to_check in inputString:
        return 'yes'
    else:
        return 'no'
        
#Component 7

#Exercise 3.7
    #a: undefined
    #b: Not counting the fact that this program will create an infinite loop, logically, this will 'no', because yesOnSelf(yesOnSelf) output 'yes'
    #c: undefined

#Exercise 3.8
def noOnSelf(P):
    if P(P) == 'no':
        return 'yes'
    else:
        return 'no'

def notYesOnSelf(P):
    if P(P) == 'yes':
        return 'no'
    else:
        return 'yes'
#P = "def P(I): return 'hi'"

#Component 8

#Exercise 3.10
#Claim: definedOnString.py cannot exist
#Proof: Suppose definedOnString.py exists. We can then write the a program
# weirdDefinedOnString.py, shown below. This program is paradoxical because 
# calling weirdDefinedOnString on itself will break if and only if it doesn't break.
# Thus a contradiction has arisen, and definedOnString cannot exist.
def definedOnString(P, I):
    if P(I): 
        return 'yes'
    else:
        return 'no'

def weirdDefinedOnString(inputString):
    if definedOnString(inputString, inputString) == 'yes':
        return 1 / 0
    else:
        return 'yes'

weirdDefinedOnString(rf('WeirdDefinedOnString.py'))

#Exercise 3.11
#Claim: longerThan10.py cannot exist
#Proof: Suppose longerThan10.py exists. We can then write a program 
#weirdLongerThan10.py, shown below. This program is paradoxical because calling 
#weirdLongerThan10.py on itself will return 'no' if and only if it is longer than 10.
#Thus a contradiction has arisen, and longerThan10.py.
def weirdLongerThan10(inputString):
    if longerThan10(inputString, inputString) == 'yes':
        return 'no'
    else:
        return 'yes'

#Exercise 3.12
#Claim: startsWithZ.py cannot exist
#Proof: Suppose startsWithZ.py exists. We can then write a program 
#weirdStartsWithZ.py, shown below. This program is paradoxical because calling 
#weirdStartsWithZ.py on itself will return 'no' if and only if it starts with Z.
#Thus a contradiction has arisen, and startsWithZ.py cannot exist.
def weirdStartsWithZ(inputString):
    if startsWithZ(inputString, inputString) == 'yes':
        return 'no'
    else:
        return 'yes'

#Exercise 3.13
# A program that takes in a function and an input as a parameter, and returns 'yes' if and only if
# the length of P(I) is even, 'no' otherwise is an impossible program.


# ~~SOLO~~
#Component 9

#Exercise 3.14
# there must be a paradoxical statement that forces the program into a contradiction. That is not the case with this proof. 