
def is_multiple_of_3(number):
    return 0 == number % 3


def is_multiple_of_5(number):
    return 0 == number % 5


def find_all_multiples_of_3_and_5_of(number):
    list_of_multiples = []
    for i in range(1, number):
        if is_multiple_of_5(i) or is_multiple_of_3(i):
            list_of_multiples.append(i)
    return list_of_multiples


def sum_all_multiple_for_a_given_number(number):
    return sum(find_all_multiples_of_3_and_5_of(number))

if __name__ == "__main__":
    print(sum_all_multiple_for_a_given_number(1000))