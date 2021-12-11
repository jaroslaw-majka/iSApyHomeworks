import pytest
from rectangular_triangle.rectangular_triangle import rectangular_triangle_calculator


def test_rectangular_triangle_calculator_input_type():
    value_a = 'a'
    value_b = 'b'
    with pytest.raises(ValueError):
        rectangular_triangle_calculator(value_a, value_b)


def test_rectangular_triangle_calculator_correct_calculation():
    value_a = 3
    value_b = 4
    expected = 5
    result = rectangular_triangle_calculator(value_a, value_b)
    assert result == expected


def test_rectangular_triangle_calculator_correct_calculation_high_numbers():
    value_a = 600
    value_b = 800
    expected = 1000
    result = rectangular_triangle_calculator(value_a, value_b)
    assert result == expected
