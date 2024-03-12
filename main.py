def factRecursion(n):
    print(n)
    if n == 1:
        return 1

    else:
        return n * factRecursion(n-1)

print(factRecursion(5))
