import sys


def check_input(data):
    for i in range(1, len(sys.argv)):
        found = False
        for row in data:
            if row[1] == sys.argv[i]:
                found = True
        if not found:
            exit(84)
