from Problem3 import is_prime

__author__ = 'erlafont'



def find_all_x_prime_numbers(number_of_prime):
    primes = []
    index = 2
    while(len(primes) < number_of_prime):
        if is_prime(index):
            primes.append(index)
        index += 1
    return primes



if __name__ == '__main__':
    print(__file__, " is main!")
    print(find_all_x_prime_numbers(10001)[-1])
else:
    print(__file__, " is loaded!")