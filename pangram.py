# 4 Check if a string is a pangram
import string

def pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    cleaned_sentence = ''
    for char in sentence.lower():
        if char.isalpha():
            cleaned_sentence += char
    unique_chars = set(cleaned_sentence)
    return alphabet.issubset(unique_chars)

print(pangram('The quick brown fox jumps over the lazy dog'))
print(pangram('Hello, world'))
