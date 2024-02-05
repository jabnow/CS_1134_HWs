#question 4 part a
def ten_powers(n=10):
    return(list(n**i for i in range(0, 6)))

print(ten_powers())

#question 4 part b
def adj_multiplier(i):
    return(list(i*(i+1) for i in range(0, 10)))

print(adj_multiplier(0))

#question 4 part c
# def alphabet():
#     return(list(map(chr, range(97, 123))))
#is this legal???

#attempt 2: q4c
# import string
# def alphabet2():
#     return(list(string.ascii_lowercase))

#attempt 3: q4c by list comprehension
def alphabet():
    return(list(chr(i) for i in range(97, 124)))
print(alphabet())