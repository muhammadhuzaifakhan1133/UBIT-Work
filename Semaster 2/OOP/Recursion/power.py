def pow(x, n):
    if n==0:
        return 1
    elif (n > 0):
        return x*pow(x, n-1)
    else:
        n = abs(n)
        return 1/(x*pow(x, n-1))

a = pow(2, -98)
print(a)