#!/usr/bin/python

import os
import random
import re
import sys

wordlist = {}


def build_markov_chain(word):
    sys.stdout.write(word + ' ')
    word = word.lower()
    new = random.choice(wordlist[word])
    if word[-1] != '.':
        build_markov_chain(new)
    else:
        print()


if len(sys.argv) == 1:
    if os.path.isfile('training_data.txt'):
        filename = 'training_data.txt'
    else:
        print('Error: No training data found!')
        sys.exit()
else:
    filename = sys.argv[1]

# read in file and format it
buffer = ''
with open(filename) as file:
    for line in file:
        for char in line:
            if re.match("[\w\s.]", char) is not None:
                if char != '\n':
                    buffer += char
                else:
                    buffer += ' '
words = buffer.split()
for i, word in enumerate(words):
    if word == '':
        del words[i]
words = [x.lower() for x in words]

# use list of words for training
for i, word in enumerate(words):
    try:
        if word not in wordlist:
            wordlist[word] = [words[i + 1]]
        else:
            wordlist[word] += [words[i + 1]]
    except BaseException:
        pass

build_markov_chain(random.choice(list(wordlist.keys())).title())
