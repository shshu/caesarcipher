#!/usr/bin/env python
from argparse import ArgumentParser
from collections import defaultdict

import operator


class Histogram(object):
    def __init__(self, data, is_word):
        if is_word:
            self.data = data.split()
        else:
            self.data = data.strip()

    def print_frequency(self):
        self.pprint(self.frequency())

    def frequency(self):
        return self.frequency()

    def pprint(self, freq):
        for item in sorted(freq.items(), key=operator.itemgetter(1)):
            print item

    def frequency(self):
        freq = defaultdict(int)
        for element in self.data:
            freq[element] += 1
        return freq


def get_parse_args():
    parser = ArgumentParser(description="accepts a file name from the user, builds a frequency listing")
    parser.add_argument("-i", dest="filename", required=True,
                        help="input file with two matrices", metavar="FILE")
    parser.add_argument("-w", dest="word", required=False,
                        help="frequency listing by words", action='store_true')
    return parser.parse_args()


def main():
    args = get_parse_args()
    try:
        with open(args.filename, 'r') as f:
            data = f.read()
            histogram = Histogram(data, args.word)
            histogram.print_frequency()
    except EnvironmentError:
        print 'Error: failed to handle file'


if __name__ == "__main__":
    main()