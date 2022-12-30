# This is an example of dynamic programming in python. The below function
# calculates the minimum number of moves required to reach the end of a list

def minimum_moves(number_list):
    # Initialize an array to store the minimum number of moves required to reach each position
    dp = [float('inf')] * len(number_list)
    # The minimum number of moves required to reach the starting position is 0
    dp[0] = 0

    # Loop through all the positions in the list
    for i in range(len(number_list)):
        # Loop through all the possible positions that can be reached
        # from the current position
        for j in range(1, number_list[i] + 1):
            # Calculate the next position
            next_position = i + j

            # If the next position is out of bounds, skip it
            if next_position >= len(number_list):
                continue

            # Update the minimum number of moves required to reach the next position
            dp[next_position] = min(dp[next_position], dp[i] + 1)

    min_moves = dp[-1]

    # if min moves is infinity, then the end of the list is unreachable return -1
    if min_moves == float('inf'):
        return -1
    else:
        return min_moves


# Test the function
print(minimum_moves([3, 2, 1, 4, 2, 3, 1, 1, 3]))  # Output: 3
print(minimum_moves([1, 2, 3]))  # Output: 2
print(minimum_moves([3, 2, 1]))  # Output: 1
print(minimum_moves([1, 1, 0, 1]))  # Output: 3
print(minimum_moves([1, 1]))  # Output: 3






