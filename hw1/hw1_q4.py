#question 4 part a
def ten_powers(n=10):
    return(list(n**i for i in range(0, 6)))

#question 4 part b
def adj_multiplier(i):
    return(list(i*(i+1) for i in range(0, 10)))

#part c by list comprehension
def alphabet():
    return(list(chr(i) for i in range(97, 124)))