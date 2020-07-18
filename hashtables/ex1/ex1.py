def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Set up a hash table for weights and their indexes
    indexes = {}

    # Iterate through the weights
    for i in range(length):
        if weights[i] not in indexes:
            # store the index
            indexes[weights[i]] = i
        else:
            #check if the weight plus itself equals the limit
            if limit - weights[i] == weights[i]:
                # Then return the current index and stored index
                return (i, indexes[weights[i]])

       # Calculate the complement
        complement = limit - weights[i]

        # If the complement exists and is not equal to itself
        if complement in indexes and complement != weights[i]:
            # Return the indexes of the weights, sorted in reverse order
            return sorted((indexes[complement], indexes[weights[i]]), reverse=True)

    # Otherwise there is no pair that adds up to the limit
    return None


#print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
#print(get_indices_of_item_weights([4, 4], 2, 8))
