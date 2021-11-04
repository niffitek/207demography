from .error import check_input
from .file import load_csv
from.output import print_countries, fit1, fit2, correlation


def main():
    data = load_csv()
    check_input(data)
    print_countries(data)
    fit1(data)
    fit2(data)
    correlation(data)


