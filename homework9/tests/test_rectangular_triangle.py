from rectangular_triangle.rectangular_triangle import rectangular_triangle_calculator


def test_rectangular_triangle_calculator_input_type():
    value_a = 'a'
    value_b = 'b'
    result = rectangular_triangle_calculator(value_a, value_b)
    assert result == ValueError
