__author__ = 'erlafont'




def sum_of_the_sqare(high_number):
    return sum(x**2 for x in range(1,high_number+1))


def square_of_the_sum(high_number):
    return sum(x for x in range(1,high_number+1))**2


def difference_of_square_and_sum(high_number):
    return square_of_the_sum(high_number) - sum_of_the_sqare(high_number)

if __name__ == '__main__':
    print(__file__, " is main!")
    print(difference_of_square_and_sum(100))
else:
    print(__file__, " is loaded!")