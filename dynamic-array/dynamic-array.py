def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        t, x, y = query
        idx = (x ^ lastAnswer) % n

        if t == 1:
            arr[idx].append(y)

        elif t == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)

    return result


# Local Test Case 1
n1 = 2
queries1 = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1]
]

print("Test Case 1:", dynamicArray(n1, queries1))


# Local Test Case 2
n2 = 2
queries2 = [
    [1, 0, 10],
    [1, 1, 20],
    [2, 0, 0],
    [1, 1, 30],
    [2, 1, 1]
]

print("Test Case 2:", dynamicArray(n2, queries2))