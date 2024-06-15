
# 3. Find most frequent character in a string
def most_frequent_char(string):
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    max_freq = 0
    most_frequent_char = ''
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_char = char
    return most_frequent_char

print(most_frequent_char('11189'))  
print(most_frequent_char('hello'))  
