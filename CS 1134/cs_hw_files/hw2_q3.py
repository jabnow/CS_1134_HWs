def factors(num):
    """
    returns a sorted generator with runtime theta(sqrt(n))
    """
    i = 1
    for i in range(i,num+1):
        if not num%i:
            yield i
def main():
    for curr_factor in factors(100):
        print(curr_factor, end=' ')
