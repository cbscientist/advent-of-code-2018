"""
Advent of Code 2018
Day 2
https://adventofcode.com/2018/day/2
"""


def getIDSFromFile(scanned_ids_file):
    """
    Takes a newline-delimited files of ids
    and returns a list of corresponding strings.
    """
    with open(scanned_ids_file, "r") as infile:
        scanned_ids = infile.read().split("\n")
    return scanned_ids


def checksum(scanned_ids):
    """
    Takes a list of id strings and computes
    a rudimentary checksum.
    """
    num_twos = 0
    num_threes = 0

    for box_id in scanned_ids:
        has_two = False
        has_three = False

        letters = set(box_id)
        for letter in letters:
            letter_count = box_id.count(letter)
            if letter_count == 2:
                has_two = True
            elif letter_count == 3:
                has_three = True

        if has_two is True:
            num_twos += 1
        if has_three is True:
            num_threes += 1

    checksum = num_twos * num_threes

    return checksum


def findCorrectIDS(scanned_ids):
    """
    Takes a list of ids and determines
    if there are two ids in the set that 
    are only 1 letter off from one another.
    """

    matching_ids = [None, None]

    for box_id in scanned_ids:
        for other_id in scanned_ids:

            num_matched_letters = 0
            for index, letter in enumerate(box_id):
                if box_id[index] == other_id[index]:
                    num_matched_letters += 1

            if num_matched_letters == len(box_id) - 1:
                matching_ids = [box_id, other_id]
                break

    return matching_ids


def getSharedLetters(matching_ids):
    """
    Takes a pair of matching ids and returns the letters
    shared between the two.
    """
    for index, pair in enumerate(zip(matching_ids[0], matching_ids[1])):
        if len(set(pair)) > 1:
            letter_location = index
            break

    shared_letters = matching_ids[0][:letter_location] + matching_ids[0][letter_location+1:]

    return shared_letters
