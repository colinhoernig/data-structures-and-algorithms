# Find the pairs of numbers in a list that sum to k
def pair_sum(arr, k):
    # edge case, return early if less than two elements
    if len(arr) < 2:
        return

    # tracking sets
    seen = set() # keeps numbers seen
    output = set() # keeps output pairs

    # loop through the entire list of numbers
    for number in arr:
        # set the target difference
        # which is the difference between k and
        # the current value of number
        target = k - number

        # check if target difference is in the set of seen numbers
        # if it is, then we have a pair sum
        # if it isn't, then we add it to the set of seen numbers
        if target not in seen:
            seen.add(number)
        else:
            # add a tuple pair to the output set
            output.add((min(number, target), max(number, target)))

    # finally, print the pairs found
    print '\n'.join(map(str, list(output)))

pair_sum([1,3,2,2], 4)