
# %%
 
import csv
file = open("corrupted_files.txt", "r")
data = list(csv.reader(file, delimiter="\t"))
file.close()

# %%
