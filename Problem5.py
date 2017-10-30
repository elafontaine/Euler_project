from Problem3 import is_prime

__author__ = 'erlafont'




def find_lowest_multiple(highest_divisor):
    number = 1
    for index in range(1,highest_divisor):
        if is_prime(index):
            number *= index

    official_number = number
    while(not is_divisible_by_all_number_under(highest_divisor,official_number)):
        official_number += number
    return official_number


def is_divisible_by_all_number_under(highest_divisor, number):
    for index in range(1,highest_divisor):
        if number % index != 0:
            return False
    return True
if __name__ == '__main__':
    print(__file__, " is main!")
    print(find_lowest_multiple(20))
else:
    print(__file__, " is loaded!")