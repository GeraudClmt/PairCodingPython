from com.campus.src.PairCodingResolution.FizzBuzz import convert, reformat_table

def test_convert():
    assert convert(3) == "Fizz"
    assert convert(7) == 7
    assert convert(5) == "Buzz"
    assert convert(15) == "FizzBuzz"
    assert convert(100) == "Buzz"


def test_sorted_list():
    assert reformat_table([1,2,3,4,5]) == [1,2,"Fizz",4,"Buzz"]
    assert reformat_table([53,35]) == ["FizzBuzz","FizzBuzzBuzz"]