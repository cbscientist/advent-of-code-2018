#!/usr/bin/env python
"""
Advent of Code 2018
https://adventofcode.com/2018/
"""

import argparse
from day_01 import frequencies
from day_02 import inventory_management


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", "-f", help="specify input file")
    parser.add_argument("--filetype", "-ft", help="specify file type")
    args = parser.parse_args()

    if args.filetype == "frequency":
        frequency_changes = frequencies.getFrequenciesFromFile(args.infile)

        resulting_frequency = frequencies.calculateResultingFrequency(frequency_changes)
        print(
            "The resulting frequency from one pass of changes is {}".format(
                resulting_frequency
            )
        )

        duplicate_frequency = frequencies.findDuplicateFrequency(frequency_changes)
        print("The first duplicate frequency found is {}".format(duplicate_frequency))

    elif args.filetype == "inventory":
        scanned_ids = inventory_management.getIDSFromFile(args.infile)

        checksum = inventory_management.checksum(scanned_ids)
        print("The checksum of the scanned ids is {}".format(checksum))

        correct_box_ids = inventory_management.findCorrectIDS(scanned_ids)
        print(
            "The two correct box IDs are {} and {}".format(
                correct_box_ids[0], correct_box_ids[1]
            )
        )

        shared_letters = inventory_management.getSharedLetters(correct_box_ids)
        print(
            "The letters shared between the two correct box IDs are {}".format(
                shared_letters
            )
        )
