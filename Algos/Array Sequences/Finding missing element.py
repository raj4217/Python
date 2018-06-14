'''
One possible solution is computing the sum of all the numbers in arr1 and arr2, and subtracting arr2’s sum from array1’s sum. The difference is the missing number in arr2. However, this approach could be problematic if the arrays are too long, or the numbers are very large. Then overflow will occur while summing up the numbers.
'''


def finder(arr1, arr2):

    # Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    # Otherwise return last element
    return arr1[-1]


import collections


def finder2(arr1, arr2):

    # Using default dict to avoid key errors
    d = collections.defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        d[num] += 1

    # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num

        # Otherwise, subtract a count
        else:
            d[num] -= 1


def finder3(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
        print result

    return result
