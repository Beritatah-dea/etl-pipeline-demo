import csv


def extract_data(path="data/input.csv"):
    rows = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            rows.append(row)

            ## this changes are done to test feature extract step branch.
            ## this is second change done to test feature extract step branch.

    return rows