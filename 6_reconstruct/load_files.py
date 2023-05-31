
# %%
import csv

def load_data():
    file = open("corrupted_files.txt", "r")
    data = list(csv.reader(file, delimiter="\n"))
    file.close()

    # %%
    list_to_work_with = []

    for outer in data:
        for inner in outer:
            #print(inner)
            res = inner.strip("][").replace("'","").split(', ')
            list_to_work_with.append(res)

    return list_to_work_with
    # %%

    len(list_to_work_with)
    len(list_to_work_with[0])