__author__ = 'erlafont'

from Problem3 import is_prime


def find_all_prime_under_x(number):
    array = []
    for index in range(2,number):
        if is_prime(index):
            array.append(index)
    return array

if __name__ == '__main__':
    print(__file__, " is main!")
    print(sum(find_all_prime_under_x(2000000)))
else:
    print(__file__, " is loaded!")

