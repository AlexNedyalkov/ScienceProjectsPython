import string
import numpy as np
import matplotlib.pyplot as plt
import re
import requests

# get the text from the internet
book = requests.get('http://www.gutenberg.org/files/35/35-0.txt')
text = book.text

# character strings to replace with space
strings2replace = [
                 '\r\n\r\nâ\x80\x9c', # new paragraph
                 'â\x80\x9c',         # open quote
                 'â\x80\x9d',         # close quote
                 '\r\n',              # new line
                 'â\x80\x94',         # hyphen
                 'â\x80\x99',         # single apostrophe
                 'â\x80\x98',         # single quote
                 '_',                 # underscore, used for stressing
                 ]


# user regular expression to replace those string with space
for item in strings2replace:
    regexp = re.compile(r'%s'%item)
    text = regexp.sub(' ', text)

# word distribution
words = text.split(' ')
wordlengths = np.zeros(len(words))

for wordi in range(len(words)):
    wordlengths[wordi] = len(words[wordi])

plt.hist(wordlengths, bins =30)
plt.xlabel('Word length')
plt.ylabel('Word count')
plt.show()

# letter frequencies
letters = string.ascii_lowercase
letter_count = np.zeros(len(letters))
counter = 0
for i in letters:
    letter_count[counter] = text.lower().count(i)
    counter += 1
plt.bar(range(len(letters)), letter_count)
plt.xlabel('Letter')
plt.ylabel('Count')
plt.show()

letter_prob = letter_count/sum(letter_count)
entropy = -sum(letter_prob * np.log2(letter_prob + np.finfo(float).eps))
plt.bar(range(len(letters)), letter_prob)
plt.xlabel('Letter')
plt.ylabel('Probability')
plt.title(f"Entropy: {entropy:.2f}")
plt.show()