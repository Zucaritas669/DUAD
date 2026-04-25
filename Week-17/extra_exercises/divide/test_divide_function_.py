import pytest
from divide_function_ import divide

def test_divide_equals_five():
    #AAA

    #Arrange
    num1 = 10
    num2 = 2

    #Act
    result = divide(num1,num2)

    #Assert
    assert result == 5.0


def test_divide_by_0_trows_error():
    #AAA

    #Arrange
    num1 = 10
    num2 = 0

    #Act / #Assert
    with pytest.raises(ValueError):
        divide(num1,num2)



def test_divide_by_string_trows_error():
    #AAA

    #Arrange
    num1 = 10
    num2 = "Hola"

    #Act / #Assert
    with pytest.raises(TypeError):
        divide(num1,num2)


