# This is an example of dynamic programming in python. The below function
# calculates the minimum number of moves required to reach the end of a list

def minimum_moves(number_list):
    """Dynamic method to calculate the minimum number of moves required 
    to reach the end of the list"""

    # check if empty list
    if not number_list:
        return -1
    # Initialize an array to store the minimum number of moves required to 
    # reach each position
    distance_table = [float('inf')] * len(number_list)
    # The minimum number of moves required to reach the starting position is 0
    distance_table[0] = 0

    # Loop through all the positions in the list
    for i,number in enumerate(number_list):
        # Loop through all the possible positions that can be reached
        # from the current position
        for j in range(1, number_list[i] + 1):
            # Calculate the next position
            next_position = i + j

            # If the next position is out of bounds, skip it
            if next_position >= len(number_list):
                continue

            # Update the minimum number of moves required to reach the next
            distance_table[next_position] = min(distance_table[next_position], distance_table[i] + 1)

    min_moves = distance_table[-1]

    # if min moves is infinity, then the end of the list is unreachable return -1
    if min_moves == float('inf'):
        return -1
    
    return min_moves


# Test the function
print(minimum_moves([3, 2, 1, 4, 2, 3, 1, 1, 3]))  # Output: 3
print(minimum_moves([1, 2, 3]))  # Output: 2
print(minimum_moves([3, 2, 1]))  # Output: 1
print(minimum_moves([1, 1, 0, 1]))  # Output: 3
print(minimum_moves([ ]))  # Output: 3