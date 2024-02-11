def printStats(t):
    """ Reads lines containing multiple numbers from file; calculates and prints
    how many numbers, the average, and the largest number
    Args: t (str): File name
    Returns: None (prints to console)"""
    file = open(t, "r")

    # initalize vars
    count = 0
    total = 0
    largest = 0
    lineNum = 0

    # loop over lines in file
    for line in file:
        lineNum += 1
        # convert line to list of ints
        line = line.split() #space seperated

        # list for storing numbers in line
        numsList = []

        # loop over numbers in line
        for number in line:
            # convert number to int
            number = int(number)
            # add number to list
            numsList.append(number)
            count += 1
            total += number # used for average
            if number > largest:
                largest = number
        
        # print stats using decorator
        print(f"Line {lineNum}: {numsList} -> count: {count}, average: {total/count}, largest: {largest}")

printStats("numbers.txt")