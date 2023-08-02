def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while n!=1:
        print(n)
        if n%2==0:
            n= n//2
        else:
            n = (n*3)+1
        i+=1

    print(n)
    return i 
print(hailstone(10))
print(hailstone(1))