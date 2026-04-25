import pytest
from bubble_sort_ import bubble_sort

def test_small_list():
    #AAA

    #Arrange
    test_list = [9,8,7,6,5,4,3,2,1]

    #Act
    bubble_sort(test_list)

    #Assert
    assert test_list == [1,2,3,4,5,6,7,8,9]



def test_small_list_grater_than_100_elements():
    #AAA

    #Arrange
    test_list = list(range(100,0,-1))

    #Act
    bubble_sort(test_list)

    #Assert
    assert test_list == list(range(1,101))



def test_empty_list():
    #AAA

    #Arrange
    test_list = []

    #Act 
    bubble_sort(test_list)

    #Assert
    assert test_list == []


def test_it_does_not_work_without_list():
    #AAA

    #Arrange
    test_list = "Hola" 

    #Act  #Assert
    with pytest.raises(TypeError):
        bubble_sort(test_list)

