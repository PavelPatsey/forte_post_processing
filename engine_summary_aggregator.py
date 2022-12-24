import os
from pprint import pprint
import csv

DATA_PATH = "."


def get_files_paths():
    files_paths = []
    for root, dirs, files in os.walk(DATA_PATH):
        for filename in files:
            if filename == "engine_summary.csv":
                files_paths.append(root + "/" + filename)
    files_paths.sort()

    return files_paths


files_paths = get_files_paths()
# pprint(files_paths)

# формирование первого столбца
data = []
with open(files_paths[0], newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
        data.append(row[0:1])
pprint(data)


# чтение
# with open('./test_data/uov_05/engine_summary.csv', newline='') as csvfile:

#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

#     for row in spamreader:

#         print(', '.join(row))


# запись
# import csv

# # field names
# fields = ["Name", "Branch", "Year", "CGPA"]

# # data rows of csv file
# rows = [
#     ["Nikhil", "COE", "2", "9.0"],
#     ["Sanchit", "COE", "2", "9.1"],
#     ["Aditya", "IT", "2", "9.3"],
#     ["Sagar", "SE", "1", "9.5"],
#     ["Prateek", "MCE", "3", "7.8"],
#     ["Sahil", "EP", "2", "9.1"],
# ]

# # name of csv file
# filename = "university_records.csv"

# # writing to csv file
# with open(filename, "w") as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)

#     # writing the fields
#     csvwriter.writerow(fields)

#     # writing the data rows
#     csvwriter.writerows(rows)
