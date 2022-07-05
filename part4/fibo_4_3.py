def fibo(N):
    result = (1/5**0.5) * ((((1+(5**0.5))/2)**N) - (((1-(5**0.5))/2)**N))
    return result


def fibo2(N):
    if (N == 0):
        return 0
    elif (N == 1):
        return 1

    result = fibo2(N-1) + fibo2(N-2)
    return result


print(fibo(20))
print(fibo2(20))
