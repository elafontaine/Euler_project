__author__ = 'erlafont'






def fib(TermNumber):
    if TermNumber <= 3:
        return TermNumber
    else:
        return fib(TermNumber - 1) + fib(TermNumber -2)


def reverse_fib(fibonnaci_value):
    i = 0
    while fibonnaci_value > fib(i) and fib(i+1) <= fibonnaci_value:
        i += 1
    return i


def even_fibonacci(term_number,list_to_append_to):
    for i in range(1,term_number+1):
        if fib(i) % 2 == 0 :
            list_to_append_to.append(fib(i))
    return list_to_append_to


def sum_even_fib_of_value(value):
    return sum(even_fibonacci(reverse_fib(value), []))

if __name__ == '__main__':
    print(__file__, " is main!")
    print(sum_even_fib_of_value(4000000))
else:
    print(__file__, " is loaded!")