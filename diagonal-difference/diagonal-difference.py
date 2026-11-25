def diagonalDifference(arr):
    n = len(arr)

    primary = 0
    secondary = 0

    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - 1 - i]

    return abs(primary - secondary)


# Local Test Case 1
arr1 = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print("Test Case 1:", diagonalDifference(arr1))


# Local Test Case 2
arr2 = [
    [1, 2],
    [3, 4]
]

print("Test Case 2:", diagonalDifference(arr2))