def multiply_by_three_plus_one(x):
    return 3 * x + 1


def get_chain_for_x(x):
    chain = []
    while x != 1:
        chain.append(x)
        if x % 2 == 0:
            x = x / 2
        else:
            x = multiply_by_three_plus_one(x)
    return chain

