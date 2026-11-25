def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]


# Local Test Case 1
a1 = [5, 6, 7]
b1 = [3, 6, 10]

print("Test Case 1:", compareTriplets(a1, b1))


# Local Test Case 2
a2 = [17, 28, 30]
b2 = [99, 16, 8]

print("Test Case 2:", compareTriplets(a2, b2))