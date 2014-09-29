#!/usr/bin/env python3

import argparse
import sys
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    description = """description=This script reads in a file with a list of sentences
        and checks whether the length exceeds a specific length"""
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-i', '--input', dest='input_file', action='store', required=True,
        help='specify the input file')
    parser.add_argument('-l', '--length', dest='length', default=160, action='store', required=False,
        help='specify the maximum allowed line length')

    args = parser.parse_args()

    print(args)

    sentences = read_urls(args.input_file)

    max_length = int(args.length)

    check_length(sentences, max_length)

    return 0


def read_urls(input_file):
    file = open(input_file)
    lines = file.readlines()
    file.close

    sentences = []
    for line in lines:
        sentences.append(line.replace('\n', ''))

    return sentences


def check_length(sentences, max_length):
    for index, sentence in enumerate(sentences):
        length = len(sentence)
        print(index, end='')
        print(":", end='')
        print("\t", end='')
        print(length, end='')
        if (length > max_length):
            print("\t -> Too long!")
        else:
            print('')

if __name__ == '__main__':
    sys.exit(main())
