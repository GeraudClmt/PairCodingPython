
def convert(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return  "Buzz"

    return number

def test_convert():
    assert convert(3) == "Fizz"
    assert convert(7) == 7
    assert convert(5) == "Buzz"
    assert convert(15) == "FizzBuzz"
    assert convert(100) == "Buzz"

if __name__ == "__main__":
    pass