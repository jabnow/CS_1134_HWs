# QUESTION 6
def appearances(s, low, high):
    # base: end dictionary
    if low > high:
        return {}
    # step: adding new key : val to dictionary
    mydict = appearances(s, low, high-1)
    # step: assume that the letter is already in the dictionary
    if s[high] in mydict:
        mydict[s[high]] += 1
    # step: if it's a new letter then add it to the dictionary
    else:
        mydict[s[high]] = 1
    return mydict
