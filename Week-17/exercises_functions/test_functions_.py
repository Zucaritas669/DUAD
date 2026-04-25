import pytest
from functions_exercises_ import sum_of_list, reverse_text, count_capital_letter, sort_hyphenated_string, get_prime_numbers


# ─── 1. sum_of_list ───────────────────────────────────────────────

def test_sum_all_elements_in_the_list():
    #Arrange
    test_list = [4, 6, 2, 29]
    #Act
    result = sum_of_list(test_list)
    #Assert
    assert result == 41

def test_sum_all_zeros():
    #Arrange
    test_list = [0, 0, 0]
    #Act
    result = sum_of_list(test_list)
    #Assert
    assert result == 0

def test_sum_negative_numbers():
    #Arrange
    test_list = [-3, -2, 5]
    #Act
    result = sum_of_list(test_list)
    #Assert
    assert result == 0


# ─── 2. reverse_text ─────────────────────────────────────────────

def test_reverse_text():
    #Arrange
    text = "if you do vibe coding , you are not a real developer"
    #Act
    result = reverse_text(text)
    #Assert
    assert result == "repoleved laer a ton era uoy , gnidoc ebiv od uoy fi"

def test_reverse_text_simple():
    #Arrange
    text = "Hola mundo"
    #Act
    result = reverse_text(text)
    #Assert
    assert result == "odnum aloH"

def test_reverse_text_single_word():
    #Arrange
    text = "python"
    #Act
    result = reverse_text(text)
    #Assert
    assert result == "nohtyp"


# ─── 3. count_capital_letter ─────────────────────────────────────

def test_counts_uppercase():
    #Arrange
    text = "ABC"
    #Act
    result = count_capital_letter(text)
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
    #Arrange
    text = "I love Nación Sushi!"
    #Act
    result = count_capital_letter(text)
    #Assert
    assert result == (3, 13)


# ─── 4. sort_hyphenated_string ───────────────────────────────────

def test_sort_hyphenated_basic():
    #Arrange
    text = "python-variable-funcion-computadora-monitor"
    #Act
    result = sort_hyphenated_string(text)
    #Assert
    assert result == "computadora-funcion-monitor-python-variable"

def test_sort_hyphenated_two_words():
    #Arrange
    text = "zebra-apple"
    #Act
    result = sort_hyphenated_string(text)
    #Assert
    assert result == "apple-zebra"

def test_sort_hyphenated_already_sorted():
    #Arrange
    text = "alfa-beta-gamma"
    #Act
    result = sort_hyphenated_string(text)
    #Assert
    assert result == "alfa-beta-gamma"


# ─── 5. get_prime_numbers ────────────────────────────────────────

def test_primes_basic():
    #Arrange
    test_list = [1, 4, 6, 7, 13, 9, 67]
    #Act
    result = get_prime_numbers(test_list)
    #Assert
    assert result == [7, 13, 67]

def test_primes_no_primes():
    #Arrange
    test_list = [1, 4, 6, 8, 9]
    #Act
    result = get_prime_numbers(test_list)
    #Assert
    assert result == []

def test_primes_all_primes():
    #Arrange
    test_list = [2, 3, 5, 11]
    #Act
    result = get_prime_numbers(test_list)
    #Assert
    assert result == [2, 3, 5, 11]