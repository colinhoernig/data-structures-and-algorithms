# reverse a sentences words
def reverse_words(s):
    words = []
    length = len(s)

    i = 0
    while i < length:
        if s[i] != ' ':
            word_start = i
            while i < length and s[i] != ' ':
                i += 1
            
            words.append(s[word_start:i])
        
        i += 1

    return ' '.join(reversed(words))

# ...and a shorter Pythonic version (boom! one liner!)
def reverse_words2(s):
    return ' '.join(reversed(s.split()))

print reverse_words('This is a test ')
print reverse_words2( ' This is a test ')