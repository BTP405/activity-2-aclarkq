def wordCount(t):
    """ Read words from a file and track their frequency and which line numbers they show up on.
        Args: t (str): File name
        Returns: frequency (dict): Dictionary of words and their corresponding line numbers"""
    # file = open(t, "r")

    # frequency = {}

    # for word in file:
    #     i += 1
    #     if word in frequency:
    #         # add line number to list
    #         frequency[word].append(i)
    #     else:
    #         frequency[word] = [i]

    # return frequency

    with open(t, "r") as file:
        words = file.readlines();

    # remove new line characters
    word = (x.strip().lower() for x in words)

    frequency = {}

    lineNum = 0

    for x in word:
        lineNum += 1
        if x in frequency:
            frequency[x].append(lineNum)
        else:
            frequency[x] = [lineNum]

    return frequency

def tester(filename):
    """ tester function; tests wordCount
        Args: filename
        Returns: None (prints to console)"""
    frequency = wordCount(filename)
    print(frequency)

tester("words.txt")