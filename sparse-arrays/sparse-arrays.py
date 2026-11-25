def matchingStrings(strings, queries):
    frequency = {}

    for string in strings:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1

    result = []

    for query in queries:
        result.append(frequency.get(query, 0))

    return result


# Local Test Case 1
strings1 = ["aba", "baba", "aba", "xzxb"]
queries1 = ["aba", "xzxb", "ab"]

print("Test Case 1:", matchingStrings(strings1, queries1))


# Local Test Case 2
strings2 = ["def", "de", "fgh"]
queries2 = ["de", "lmn", "fgh"]

print("Test Case 2:", matchingStrings(strings2, queries2))