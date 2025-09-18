from com.campus.src.PairCodingResolution.FizzBuzz import convert, reformat_table

def test_sorted_list():
    assert reformat_table([1,2,3,4,5]) == [1,2,"FizzFizz",4,"BuzzBuzz"]
    assert reformat_table([53]) == ["FizzBuzz"]
    assert reformat_table([52, 31]) == ["Buzz", "Fizz"]
    assert reformat_table([7, 71, 19, 11, 14, 88]) == [7, 71, 19, 11, 14, 88]
    assert reformat_table([55, 30, 35]) == ["BuzzBuzzBuzz", "FizzFizzBuzz", "FizzBuzzBuzz"]

