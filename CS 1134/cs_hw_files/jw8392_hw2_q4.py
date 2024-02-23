def e_approx(n):
    """
    returns an approximation of e,
    calculated by the sum of the first (n+1)
    e = 1 + 1/i! ...1/(n+1)!
    should run in theta(n)
    """
    curr_sum = 1
    curr_product = 1
    i = 1
    while i <= n:
        curr_product *= i
        curr_sum += 1 / curr_product
        i += 1
    return curr_sum
def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)