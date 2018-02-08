__author__ = 'erlafont'



def is_pythagorian(a, b, c):
    if a ** 2 + b**2 == c**2 :
        return True
    return False

def pythagorian_numbers_for(total):
    list_of_pythagorian_numbers = []
    for c in range(total //2):
        for b in range(c,total //2 - c,-1):
            if is_pythagorian(total - c -b, b, c) and total - c <  b << 1:
                list_of_pythagorian_numbers.append([total - c -b,b,c])
    return list_of_pythagorian_numbers



if __name__ == '__main__':
    print(__file__, " is main!")
    print(pythagorian_numbers_for(1000))
    import Problem8
    print(Problem8.mul(pythagorian_numbers_for(1000)[0]))
else:
    print(__file__, " is loaded!")