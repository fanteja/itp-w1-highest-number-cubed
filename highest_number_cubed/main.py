"""This is the entry point of the program."""


def highest_number_cubed(limit):
    count = 1
    while count ** 3 < limit:
        count = count + 1
        if count ** 3 > limit:
            return count - 1