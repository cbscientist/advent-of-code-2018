
with open('day_2_input.txt', 'r') as infile:
    id_list = infile.read().split('\n')

results_dictionary = {}

for box_id in id_list:
    results_dictionary[box_id] = {}
    letters = set(box_id)
    for letter in letters:
        letter_count = box_id.count(letter)
        if letter_count == 2:
            results_dictionary[box_id]['two_letter'] = True
        elif letter_count == 3:
            results_dictionary[box_id]['three_letter'] = True


num_twos = sum([1 for result in results_dictionary if 'two_letter' in results_dictionary[result]])
num_threes = sum([1 for result in results_dictionary if 'three_letter' in results_dictionary[result]])
checksum = num_twos * num_threes

print(checksum)