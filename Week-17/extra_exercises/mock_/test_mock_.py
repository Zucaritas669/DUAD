from unittest.mock import mock_open, patch
import pytest
from mock_exercise_ import read_file_lines

def test_read_file_returns_expected_lines():
    #Arrange
    fake_content = "hola\nmundo\npython"
    expected = ["hola", "mundo", "python"]

    #Act
    with patch("builtins.open", mock_open(read_data=fake_content)):
        result = read_file_lines("fake_path.txt")

    #Assert
    assert result == expected


def test_read_file_raises_error_if_not_found():
    #Arrange
    mock = mock_open()
    mock.side_effect = FileNotFoundError

    #Act #Assert
    with patch("builtins.open", mock):
        with pytest.raises(FileNotFoundError):
            read_file_lines("archivo_inexistente.txt")