from matplotlib import pyplot as plt

def graphSnowfall(t):
    """Reads numbers from a file into a dictionary of segments of snowfall 
    heights and then graphs their occurences using matplotlib
    Args: t (str): File name
    Returns: None"""
    file = open(t, "r")

    # dictionary of snowfall heights
    snowfall_heights = {"1_10":0, 
                        "11_20":0,
                        "21_30":0,
                        "31_40":0,
                        "41_50":0}
    
    for line in file:
        # convert line to int
        line = int(line)

        if line >= 1 and line <= 10:
            snowfall_heights["1_10"] += 1
        elif line >= 11 and line <= 20:
            snowfall_heights["11_20"] += 1
        elif line >= 21 and line <= 30:
            snowfall_heights["21_30"] += 1
        elif line >= 31 and line <= 40:
            snowfall_heights["31_40"] += 1
        elif line >= 41 and line <= 50:
            snowfall_heights["41_50"] += 1

    # plot graph
    
    # graph title
    plt.title("Snowfall Height Occurences")
    
    # x-axis label
    plt.xlabel("Snowfall Height Range")
    
    # y-axis label
    plt.ylabel("Occurences")
    
    # bar labels
    labels = ["1-10", "11-20", "21-30", "31-40", "41-50"]

    # bar heights
    heights = [snowfall_heights["1_10"], 
               snowfall_heights["11_20"], 
               snowfall_heights["21_30"], 
               snowfall_heights["31_40"], 
               snowfall_heights["41_50"]]

    # plot bar graph
    plt.bar(labels, heights)
    plt.show()
            
graphSnowfall("snowfall.txt")