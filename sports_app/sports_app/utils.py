import csv


# Function to read and return CSV data
def read_csv_file(filename):
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data
