
def splitlist(numbers):
    if not numbers:
        return None, []
    min_index = numbers.index(min(numbers))
    numbers[0], numbers[min_index] = numbers[min_index], numbers[0]
    return numbers [0], numbers[1:]

    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
