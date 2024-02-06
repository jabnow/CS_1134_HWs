#question 5
def fibs(n):
    n1, n2 = 1, 1
    if n <= 0:
        yield "bruh"
    elif n <= 1:
        yield 1
    else:
        for i in range(0, n):
            yield n1
            nxt = n1 + n2
            n1, n2 = n2, nxt