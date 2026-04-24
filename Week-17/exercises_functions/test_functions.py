import pytest
from functions_exercises import sum_of_list,reverse_text,count_capital_letter

def test_sum_all_elements_in_the_list():
    #AAA

    #Arrange
    test_list = [4, 6, 2, 29]

    #Act
    result = sum_of_list(test_list)

    #Assert
    assert result == 41



def test_reverse_text():
    #AAA

    #Arrange
    text  = "if you do vibe coding , you are not a real developer"

    #Act
    result = reverse_text(text)

    #Assert
    assert result == "repoleved laer a ton era uoy , gnidoc ebiv od uoy fi"



def test_counts_uppercase():
    #Arrange
    text = "ABC"

    #Act
    result = count_capital_letter("ABC")

    #Assert
    assert result == (3, 0) 

def test_counts_lowercase():
    #Arrange
    text = "abc"

    #Act
    result = count_capital_letter(text)

    #Assert
    assert result == (0, 3)  



def test_counts_mixed():
    result = count_capital_letter("I love Nación Sushi!")
    assert result == (3, 13)