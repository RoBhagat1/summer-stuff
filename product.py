from operator import add, mul
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1
def product(n, term):

    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    amount = 1
    i=1
    while i<=n:
        amount = term(i)*amount
        i+=1
    return amount

print(product(3,triple))
print(product(3, increment))
print(product(5, square))
print(product(3, square))
print(product(5, identity))
print(product(3, identity))