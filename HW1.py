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

