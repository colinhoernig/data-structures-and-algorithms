# test data
arr1 = [5, 5, 7, 7]
arr2 = [5, 7, 7]

# O(nlogn) method to find the missing element between
# first and second array
def finder(arr1, arr2):
    # sort both arrays
    arr1.sort();
    arr2.sort();

    # loop until we find a different numbers
    # at the same loop index
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
        
    # if no difference found, return the last number
    return arr1[-1]

# Hash table solution for linear time.
import collections
def finder2(arr1, arr2):
    # create a dict for counting
    d = collections.defaultdict(int)

    # increase count each time a number appears in the second array
    for num in arr2:
        d[num] += 1 # this is why we use defaultdict (avoid key errors)

    # decrease count each time a number
    # from the first array appears in the second array
    # otherwise return num as it is the missing element
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# Cool trick to find the missing element using XOR
def finder3(arr1, arr2):
    # initialize result to 0
    result = 0

    # concatenate the lists and XOR
    # the result and current element
    for num in arr1 + arr2:
        result ^= num

    # the result is the missing element
    return result

print finder(arr1, arr2)
print finder2(arr1, arr2)
print finder3(arr1, arr2)