import csv


def load_csv():
    data = []
    with open("./207demography_data.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        for country in reader:
            data.append(country)
    return data
