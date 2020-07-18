def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Set up hash table to track counts
    # key: number, value: count
    counts = {}

    # Set up intersections list
    result = []


    # Iterate though the array of arrays
    for arr in arrays:
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

                if counts[num] == len(arrays):
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
