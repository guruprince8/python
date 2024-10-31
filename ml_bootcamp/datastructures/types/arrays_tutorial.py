import random

L = range(10000)
length = 1000000
a = [random.choice(L) for _ in range(length)]


def find_number_linear_search(source, number):
    noOfTrips = 0
    result = -1
    for x in source:
        noOfTrips = noOfTrips + 1
        if x == number:
            result = 1
            break
    print("Number of trips are", noOfTrips)
    return result


try:
    numberToSearch = int(input("Please enter number to find\n"))
    if find_number_linear_search(source=a, number=numberToSearch) == 1:
        print("{0} found".format(numberToSearch))
    else:
        print("{0} not found".format(numberToSearch))
except ValueError as err:
    print("{0} is not an integer".format(err))
