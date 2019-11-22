#!/usr/bin/env python
"""
Advent of Code 2018
Day 1
https://adventofcode.com/2018/day/1
"""

import argparse


def getFrequenciesFromFile(frequency_changes_file):
    """
    Takes a newline-delimted text file of frequency
    changes and returns a list of corresponding
    integers.
    """
    with open(frequency_changes_file, "r") as input_file:
        frequency_changes = [int(f) for f in input_file.read().split("\n")]
        return frequency_changes


def calculateResultingFrequency(frequency_changes, origin=0):
    """
    Takes a list of frequency changes and calculates
    the resulting frequency based on an origination point,
    which defaults to 0.
    """
    resulting_frequency = sum([origin] + frequency_changes)
    return resulting_frequency


def findDuplicateFrequency(frequency_changes, origin=0):
    """
    Takes a list of frequency changes and finds the first
    frequency that is traversed twice, starting from
    an assumed origin point of 0.
    """

    found_duplicate = False
    resulting_frequencies = [origin]
    current_frequency = origin

    while found_duplicate is False:
        for frequency_change in frequency_changes:
            current_frequency += frequency_change
            resulting_frequencies += [current_frequency]

            if len(set(resulting_frequencies)) != len(resulting_frequencies):
                found_duplicate = True
                duplicate_frequency = resulting_frequencies.pop()
                break

    return duplicate_frequency
