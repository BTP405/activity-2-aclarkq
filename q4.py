# stats decrator
def stats_decorator(func):
    def wrapper(line_num, nums_list, count, total, largest):
        print(f"Line {line_num}: {nums_list} -> count: {count}, average: {total/count}, largest: {largest}")
        func(line_num, nums_list, count, total, largest)
        
    return wrapper

# create decorator obj
@stats_decorator
def print_stats_decorator(line_num, nums_list, count, total, largest):
    pass # 

def printStats(t):
    """ Reads lines containing multiple numbers from file; calculates and prints
    how many numbers, the average, and the largest number
    Args: t (str): File name
    Returns: None (prints to console)"""
    file = open(t, "r")

    # initalize vars
    count = 0 # number of numbers
    total = 0 # sum of numbers
    largest = 0 # largest number
    lineNum = 0 # line number

    # loop over lines in file
    for line in file:
        lineNum += 1
        # convert line to list of ints
        line = line.split() #space seperated

        numsList = [] # list for storing numbers in line

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
        print_stats_decorator(lineNum, numsList, count, total, largest) # doesn't feel particularly efficient

printStats("numbers.txt")