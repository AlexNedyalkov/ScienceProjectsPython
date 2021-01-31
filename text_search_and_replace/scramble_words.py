import numpy as np
import string

text = "I have often wondered whether it's possible to read an entire book faster if the useless letters were removed."
letters = string.ascii_lowercase

# split the text into words
words = text.split(' ')
# randomly scramble all letters within each word
for n in range(len(words)):
    word = words[n]
    word_mid = word[1:-1]
    if len(word) > 3:
        ind_word = np.random.permutation(len(letters))[:len(word_mid)]
        new_word = word[0] + str.join('', [letters[i] for i in ind_word]) + word[-1]
        words[n] = new_word

print(str.join(' ', words))
