

with open('input_file.txt', 'r') as infile:
    id_list = infile.read().split('\n')

for box_id in id_list:
    letters = set(box_id)
    for letter in letters:
        
