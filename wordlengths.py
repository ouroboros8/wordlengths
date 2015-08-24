import sys
import argparse
import math

def max_length(wordlist):
    longest = 0
    for word in wordlist:
        length = len(word)
        if length > longest:
            longest = length
    return longest

def count_lengths(wordlist):
    longest = max_length(wordlist)
    wordlist = list(set(wordlist))
    length_counts = [0]*longest
    for word in wordlist:
        length_counts[len(word)-1] += 1
    return length_counts

def print_table(length_counts, max_lines):
    longest = len(length_counts)
    most = max(length_counts)
    most_index = length_counts.index(most)

    if max_lines < most:
        scaling_factor = max_lines/most
    else:
        scaling_factor = 1

    scaled_counts = [math.floor(count*scaling_factor)
                     for count in length_counts]

    row_format = "{:>3}" * longest
    print(row_format.format(*range(1, longest+1)))
    for row_number in range(0, max(scaled_counts)):
        row = ['*' if scaled_counts[col] != 0 else '' for col in
               range(0, longest)]
        scaled_counts = [length - 1 if length > 0 else 0
                         for length in scaled_counts]
        print(row_format.format(*row))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Make a graph of word"
                                                 " lengths.")
    parser.add_argument('wordlist', type=argparse.FileType('r'),
                        help="List of words")
    parser.add_argument('-m', type=int, help="Maximum number of lines"
                                             " for the chart to occupy.")
    args = parser.parse_args()

    wordlist = args.wordlist.read().split()

    print_table(count_lengths(wordlist), args.m)
