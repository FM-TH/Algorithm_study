import time


def tribo(N):
    if (N == 0):
        return 0
    elif (N == 1):
        return 0
    elif (N == 2):
        return 1

    result = tribo(N-1) + tribo(N-2) + tribo(N-3)

    return result


start = time.time()
print(tribo(20))
end = time.time()


print("****************")
print(end-start)
