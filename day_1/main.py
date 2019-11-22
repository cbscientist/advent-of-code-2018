#!/usr/bin/env python
"""
Advent of Code 2018
Day 1
https://adventofcode.com/2018/day/1
"""

import argparse
import frequencies


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", "-f", help="specify input file")
    args = parser.parse_args()

    frequency_changes = frequencies.getFrequenciesFromFile(args.input_file)
    resulting_frequency = frequencies.calculateResultingFrequency(frequency_changes)
    duplicate_frequency = frequencies.findDuplicateFrequency(frequency_changes)

    print(
        "The resulting frequency from one pass of changes is {}".format(
            resulting_frequency
        )
    )
    print("The first duplicate frequency found is {}".format(duplicate_frequency))
