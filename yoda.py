# 6. Yoda speaking style in a sentence
def yoda_style(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words[::-1]:
        reversed_words.append(word)
    yoda_sentence = ' '.join(reversed_words)
    return yoda_sentence

print(yoda_style('I am home'))