#question 5
def fibs(n):
    count = 0
    n1, n2 = 0, 1
    if n <= 0:
        yield "bruh"
    elif n <= 1:
        yield 1
    else:
        while count < n+1:
            yield n1
            nxt = n1 + n2
            n1, n2 = n2, nxt
            count += 1

for thing in fibs(8):
    print(thing, end=" ")