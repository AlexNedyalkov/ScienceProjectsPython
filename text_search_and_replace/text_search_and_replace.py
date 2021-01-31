import re
import string
import numpy as np

# import the file
f = open('captions_text.vtt')
text = f.read(-1)

pattern2replace = r'\n\d{1,3}\n\d\d:\d\d.\d\d\d --> \d\d:\d\d.\d\d\d\n'
regex_timestamp = re.compile(pattern2replace)

new_text = regex_timestamp.sub(' ', text)
words_list = new_text.split(' ')
for ind in range(len(words_list)):
    if len(words_list[ind]) == 4 and not words_list[ind][0] == '.':
        words_list[ind] = words_list[ind][0] + '***'
final_text = str.join(' ', words_list)
print(final_text)

