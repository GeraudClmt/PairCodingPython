from itertools import count


def reformat_table(list_of_numbers):
    sorted_list=[]
    for number in list_of_numbers:

        sorted_list.append(convert(number))
    return sorted_list
def convert(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return  "Buzz"
    count = 0
    numberstr = str(number)
    while count < len (numberstr):
        print(numberstr[count])
    return number
