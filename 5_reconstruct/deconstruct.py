# %%
import csv
file = open("../data/ekg_data/01_Ruhe.txt", "r")
data = list(csv.reader(file, delimiter="\t"))
file.close()

def extract(lst):
    return [item[0] for item in lst]

ekg_data = extract(data)

# %%
# the original file()

import random

fragment_length = 2000
number_of_segements = 500


full_dna_sequence = ekg_data
print("The final DNA sequence is {} long.".format(len(full_dna_sequence)))

list_of_fragments = []

# The seed ensures, hat everybody gets the same results, when we randomly split the data
random.seed(1)

list_of_fragments.append(full_dna_sequence[0:fragment_length])

for i in range(1,number_of_segements):
  start = random.randint(0, len(full_dna_sequence))
  end = start + fragment_length
  list_of_fragments.append(full_dna_sequence[start:end])
  #print("From {} to {}".format(start, end))

#full_dna_sequence

print("Created a list of {} subquences that are {} long.".format(number_of_segements,fragment_length))

list_of_fragments.append(full_dna_sequence[0:200])
list_of_fragments.append(full_dna_sequence[-200:])

# %%
with open('corrupted_files.txt', 'w') as fp:
    for item in list_of_fragments:
        # write each item on a new line
        fp.write(item + "\n")
    print('Done')
# %%
