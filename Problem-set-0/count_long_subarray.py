def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    if not isinstance(A, (list, tuple)) or not A:
        return 0

    count = 1
    current_length = 1
    max_increasing_length = 1

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            current_length += 1
            if (current_length == max_increasing_length):
                count += 1
            elif current_length > max_increasing_length:
                max_increasing_length = current_length
                count = 1
        else:
            current_length = 1

    return count
