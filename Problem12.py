def return_all_factors_of_number(x):
    factors = []
    for y in range(1, x):
        if x % y == 0:
            factors.append(y)
    factors.append(x)
    return factors


def generate_triangle_number():
    index = 2
    x = 1
    while True:
        yield x
        x, index = x + index, index + 1


def find_first_number_containing_x_factors(x):
    for triangle_number in generate_triangle_number():
        factors = return_all_factors_of_number(triangle_number)
        print("{}: {}".format(triangle_number,len(factors)))
        if len(factors) >= x:
            return triangle_number


if __name__ == "__main__":
    print(find_first_number_containing_x_factors(500))
