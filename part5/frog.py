N = 6
h = [30, 10, 60, 10, 60, 50]
# h = []
# print("数字を6つ入力")
# for x in range(6):
#     h.append(int(input()))

cost = [0]
cost.append(abs(h[1]-h[0]) + cost[0])

i = 2
while i < 6:
    one = abs(h[i]-h[i-1]) + cost[i-1]
    two = abs(h[i]-h[i-2]) + cost[i-2]
    if one < two:
        cost.append(one)
    else:
        cost.append(two)
    i += 1

print("\n")
print("*****************")
print(cost[-1])
