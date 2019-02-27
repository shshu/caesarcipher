#!/usr/bin/env python
from argparse import ArgumentParser
from histogram import Histogram

import heapq
import string


class CaesarCipher(object):
    LENGTH_OF_GUESS_TEXT = 50

    def __init__(self, data):
        self.data = data
        pass

    def caesar(self, text, key):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        table = string.maketrans(alphabet, shifted_alphabet)
        return text.translate(table)

    # https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
    # calculate score of the text by counting frequency of t and e
    def calculate_guess_score(self, frequency_dict):
        value = 0
        if frequency_dict.get('t'):
            value += frequency_dict.get('t')
        if frequency_dict.get('e'):
            value += frequency_dict.get('e')
        return value

    def decrypt(self):
        text = self.data[:self.LENGTH_OF_GUESS_TEXT]
        guess = []
        for key in xrange(len(string.ascii_lowercase)):
            key_text = self.caesar(text, key)
            frequency_dict = Histogram(key_text, False).frequency()
            score = self.calculate_guess_score(frequency_dict)
            heapq.heappush(guess, (score, [key, key_text]))

        while len(guess):
            print heapq.heappop(guess)[1]


def get_parse_args():
    parser = ArgumentParser(description="accepts a file name from the user")
    parser.add_argument("-i", dest="filename", required=True,
                        help="input file with two matrices", metavar="FILE")
    parser.add_argument("-k", dest="key", type=int, required=False,
                        help="Use specific key")
    return parser.parse_args()


def main():
    args = get_parse_args()
    try:
        with open(args.filename, 'r') as f:
            data = f.read()
    except EnvironmentError:
        print 'Error: failed to handle file'
        return

    caesar_cipher = CaesarCipher(data)
    if args.key is not None:
        caesar_cipher.caesar(data, args.key)

    else:
        caesar_cipher.decrypt()
        key = int(input('Please enter key guess\n'))
        print caesar_cipher.caesar(data, key)


if __name__ == "__main__":
    main()