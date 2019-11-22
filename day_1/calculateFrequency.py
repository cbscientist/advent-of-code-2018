#!/usr/bin/env python
"""
Advent of Code 2018
Day 1
https://adventofcode.com/2018/day/1
"""

import argparse


def calculateResultingFrequency(frequency_changes_file):
    """
    Calculates the resulting frequency after a sequence of frequency changes,
    outlined in a frequency list file, occur. Assumes that the starting frequency
    in this case is 0.
    """
    with open(frequency_changes_file, "r") as infile:
        resulting_frequency = sum([int(f) for f in infile.read().split("\n")])
        return resulting_frequency


if __name__ == "__main__":
    help_text = "Pass in the name of a file with newline-delimited frequency changes."
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument("--input-file", "-f", help="specify input file")
    args = parser.parse_args()

    resulting_frequency = calculateResultingFrequency(args.input_file)
    print(resulting_frequency)
