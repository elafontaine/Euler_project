__author__ = 'erlafont'

def is_palindrome(number):
    number_as_string = str(number)
    for index,segment_characters in enumerate(number_as_string):
        if number_as_string[-index - 1] != number_as_string[index]:
            return False
    return True

def find_largest_palindrome(number_of_digits):
    number1, number2 = 1,1
    for number_1 in range(10**number_of_digits,1, -1):
        for number_2 in range(10**number_of_digits,1,-1):
            if is_palindrome(number_1 * number_2) and number_1 * number_2 > number1 * number2:
                number1, number2 = number_1, number_2
    return (number1, number2)

if __name__ == '__main__':
    print(__file__, " is main!")
    print(find_largest_palindrome(3))
else:
    print(__file__, " is loaded!")