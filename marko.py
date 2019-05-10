#!/usr/bin/python

import os
import random
import re
import sys


def text_to_training_data(filename):
    # read in the file, remove special characters
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

    # strip out blank entries
    for i, word in enumerate(words):
        if word == '':
            del words[i]
    words = [x.lower() for x in words]

    wordlist = {}
    for i, word in enumerate(words):
        try:
            if word not in wordlist:
                wordlist[word] = [words[i + 1]]
            else:
                wordlist[word] += [words[i + 1]]
        except BaseException:
            pass

    return wordlist


def build_markov_chain(word, wordlist):
    sys.stdout.write(word + ' ')
    word = word.lower()
    new = random.choice(wordlist[word])
    if word[-1] != '.':
        build_markov_chain(new, wordlist)
    else:
        print('')
# read in file and format it


# use list of words for training

def main():
    wordlist = text_to_training_data('training_data.txt')
    build_markov_chain(random.choice(list(wordlist.keys())).title(), wordlist)


if __name__ == "__main__":
    main()
