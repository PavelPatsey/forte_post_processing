import csv
import os

DATA_PATH = "."
PATH_TO_WRITE = "aggregated_engine_summary.csv"


def get_files_paths():
    files_paths = []
    for root, dirs, files in os.walk(DATA_PATH):
        for filename in files:
            if filename == "engine_summary.csv":
                files_paths.append(root + "/" + filename)
    files_paths.sort()

    return files_paths


def get_data(files_paths):
    data = []

    with open(files_paths[0], newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        for row in csv_reader:
            data.append(row[0:1])

    for path in files_paths:
        with open(path, newline="") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")
            i = 0
            for row in csv_reader:
                data[i].append(row[-1].strip())
                i += 1

    return data


def write_data_to_csv(data):
    filename = PATH_TO_WRITE
    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)


def main():
    files_paths = get_files_paths()
    data = get_data(files_paths)
    write_data_to_csv(data)


if __name__ == "__main__":
    main()
