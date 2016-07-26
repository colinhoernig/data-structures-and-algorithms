# given an array of integers,
# find the largest continuous sum in an array
def largest_continuous_sum(arr):
    # if list is length 0, return 0
    if len(arr) == 0:
        return 0
    
    # init current and max sums to first number in list
    current_sum = max_sum = arr[0]

    # loop through all numbers, skipping the first
    for num in arr[1:]:
        # update the current sum to the larger of current_sum + num and num
        current_sum = max(current_sum + num, num)
        # update the max sum to the larger of current_sum or max_sum
        max_sum = max(current_sum, max_sum)

    return max_sum

print largest_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])