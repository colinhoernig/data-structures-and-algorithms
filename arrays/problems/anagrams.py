# This method checks for anagram by checking
# that two sorted strings are the same (ignoring
# whitespace and capitalization)
def anagram(s1, s2):
    # remove whitespace and lowercase all    
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

print anagram('dog', 'god')
print anagram('test', 'testing')

# This method checks for anagram by checking for
# for matching character frequencies
def anagram2(s1, s2):
    # remove whitespace and lowercase all
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # return False early if lenths are different
    if len(s1) != len(s2):
        return False

    # dict to hold frequency counts
    count = {}

    # add or update frequency count for each letter in s1
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # add or update frequency count for each letter in s2
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # check if any count is not 0 (if any count is not 0, not an anagram)
    for k in count:
        if count[k] != 0:
            return False

    # otherwise, an anagram!
    return True

print anagram2('dog', 'god')
print anagram2('test', 'testing')