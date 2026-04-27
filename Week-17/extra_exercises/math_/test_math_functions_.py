import pytest
from math_functions_ import sum_numbers,average,absolute_value

def test_sum_positive_numbers():
    #AAA

    #Arrange
    a = 67
    b = 90

    #Act
    result = sum_numbers(a,b)

    #Assert
    assert result == 157


def test_sum_negative_numbers():
    #AAA

    #Arrange
    a = -10
    b = -90

    #Act
    result = sum_numbers(a,b)

    #Assert
    assert result == -100


def test_sum_cero_numbers():
    #AAA

    #Arrange
    a = 0
    b = 85

    #Act
    result = sum_numbers(a,b)

    #Assert
    assert result == 85

#====================================

#AVERAGE
def test_average_positive():
    #AAA

    #Arrange
    test_average = [2, 4, 6]

    #Act
    result = average(test_average)

    #Assert
    assert result == 4.0


def test_average_negative():
    #AAA

    #Arrange
    test_average = [-2, -4, -6]

    #Act
    result = average(test_average)

    #Assert
    assert result == -4.0



def test_average_ceros():
    #AAA

    #Arrange
    test_average = [0, 0, 0]

    #Act
    result = average(test_average)

    #Assert
    assert result == 0.0

#====================================

#ABSOLUTE VALUE
def test_absolute_value_positive():
    #Arrange
    number = 5
    #Act
    result = absolute_value(number)
    #Assert
    assert result == 5

def test_absolute_value_negative():
    #Arrange
    number = -5
    #Act
    result = absolute_value(number)
    #Assert
    assert result == 5

def test_absolute_value_zero():
    #Arrange
    number = 0
    #Act
    result = absolute_value(number)
    #Assert
    assert result == 0





