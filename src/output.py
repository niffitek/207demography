import sys
from math import sqrt


def print_countries(data):
    print("Country: ", end="")
    countries = []
    for i in range(1, len(sys.argv)):
        for row in data:
            if row[1] == sys.argv[i]:
                countries.append(row[0])
    countries.sort()
    for country in countries:
        if country != countries[-1]:
            print(country + ", ", end="")
        else:
            print(country)


def sum_data(data):
    demography = [0] * 58
    for i in range(1, len(sys.argv)):
        for row in data:
            if row[1] == sys.argv[i]:
                for j in range(2, len(row)):
                    demography[j - 2] += int(row[j])
    return demography


def get_function_fit1(data):
    sum_population = sum(data)
    sum_years = 0
    sum_pow = 0
    sum_product = 0
    for i in range(1960, 2018):
        sum_years += i
        sum_pow += pow(i, 2)
        sum_product += data[i - 1960] * i
    m = (((2018 - 1960) * sum_product) - (sum_population * sum_years)) / ((2018 - 1960) * sum_pow - pow(sum_years, 2))
    n = (sum_population * sum_pow - sum_years * sum_product) / ((2018 - 1960) * sum_pow - pow(sum_years, 2))
    return m, n


def fit1(data):
    print("Fit 1")
    total_data = sum_data(data)
    m, n = get_function_fit1(total_data)
    if n >= 0:
        print("\tY = %.2f X + %.2f" % (m / 1000000, n / 1000000))
    else:
        print("\tY = %.2f X - %.2f" % (m / 1000000, -n / 1000000))
    res = 0
    for i in range(len(total_data)):
        func = (1960 + i) * m + n
        res += (pow(func - total_data[i], 2) / len(total_data))
    print("\tRoot-mean-square deviation: %.2f" % (sqrt(res) / 1000000))
    print("\tPopulation in 2050: %.2f" % ((2050 * m + n) / 1000000))


def get_function_fit2(data):
    sum_population = sum(data)
    sum_years = 0
    sum_pow = 0
    sum_product = 0
    for i in range(1960, 2018):
        sum_years += i
        sum_pow += pow(data[i - 1960], 2)
        sum_product += data[i - 1960] * i
    m = (((2018 - 1960) * sum_product) - (sum_years * sum_population)) / ((2018 - 1960) * sum_pow - pow(sum_population, 2))
    n = (sum_years * sum_pow - sum_population * sum_product) / ((2018 - 1960) * sum_pow - pow(sum_population, 2))
    return m, n


def fit2(data):
    print("Fit 2")
    total_data = sum_data(data)
    m, n = get_function_fit2(total_data)
    if n >= 0:
        print("\tX = %.2f Y + %.2f" % (m * 1000000, n))
    else:
        print("\tX = %.2f Y - %.2f" % (m * 1000000, -n))
    res = 0
    for i in range(len(total_data)):
        func = (1960 + i - n) / m
        res += (pow(func - total_data[i], 2) / len(total_data))
    print("\tRoot-mean-square deviation: %.2f" % (sqrt(res) / 1000000))
    print("\tPopulation in 2050: %.2f" % ((2050 - n) / m / 1000000))


def correlation(data):
    total_data = sum_data(data)
    average_data = sum(total_data) / 58
    average_years = 0
    for i in range(1960, 2018):
        average_years += i
    average_years /= 58
    deviation_data = 0
    deviation_years = 0
    for i in range(1960, 2018):
        deviation_data += pow(total_data[i - 1960] - average_data, 2)
        deviation_years += pow(i - average_years, 2)
    deviation_data /= 58
    deviation_years /= 58
    deviation_data = sqrt(deviation_data)
    deviation_years = sqrt(deviation_years)
    covariance = 0
    for i in range(1960, 2018):
        covariance += (total_data[i - 1960] - average_data) * (i - average_years)
    covariance /= 58
    print("Correlation: %.4f" % ((covariance / (deviation_data * deviation_years))))