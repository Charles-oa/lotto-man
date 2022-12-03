def NumberExist(listofNumbers, numberTofind):
    position = 0
    count = 0
    for number in listofNumbers:
        count = count + 1
        if (numberTofind == number):
            position = count
            break
    return position

numbers = []
maxNumbers = int(input('How many numbers to do you want to enter?: '))
print('Enter your ',maxNumbers, 'numbers. Hit enter to save')

numsEntered = 0

while numsEntered < maxNumbers:
    ReadNum = int(input('Enter your ' + str(numsEntered +1) + 'number: '))
    numbers.append (ReadNum)
    numsEntered = numsEntered +1
print('These are the numbers you entered: ',numbers)

choice = int(input('Enter your number to find (-1 to exit): '))
while choice != -1:
    foundPosition = NumberExist(numbers,choice)
    if (foundPosition > 0):
            print('your number ', choice, 'was found at position ',foundPosition)
    else:
            print('your number ', choice, 'was not found')

    choice = int(input('Enter number to find (-1 to exit): '))