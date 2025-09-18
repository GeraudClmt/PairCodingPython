
def reformat_table(list_of_numbers):
    sorted_list=[]
    for number in list_of_numbers:

        sorted_list.append(convert(number))
    return sorted_list


def convert(number):
    result = ""
    left = ""
    right = ""

    if number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result =  "Buzz"

    for char in str(number):
        if char == '3':
            left += "Fizz"
        elif char == '5':
            right += "Buzz"

    result = left + result + right

    if len(result) > 0:
        return result

    return number
