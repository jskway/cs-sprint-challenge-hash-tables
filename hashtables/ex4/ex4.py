def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Set up hash table
    # key: number
    # value: boolean (list contains its negation)
    has_opp = {}

    # Set up result list
    result = []

    # Iterate through the nums:
    for num in a:
        # If positive
        if num > 0:
            # If positive num not in hash table
            if num not in has_opp:
                # Initialize entry with False
                has_opp[num] = False
            # If negative version is hash
            if -num in has_opp:
                has_opp[-num] = True
                has_opp[num] = True
        # If negative
        else:
            # If negative num not in hash table
            if num not in has_opp:
                # Initialize entry with false
                has_opp[num] = False
            # If positive version is in hash table
            if abs(num) in has_opp:
                # Set value to true
                has_opp[abs(num)] = True
                has_opp[num] = True

    # Iterate through the entries
    for num, boolean in has_opp.items():
        if boolean is True and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
