import pytest
from Calculator.calculator import Calculator
class TestCalculator:

    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_sub(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_mult(self):
        # arrange
        a = 4321
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 8642
        assert result == expected

    def test_div(self):
        # arrange
        a = 333
        b = 3
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 111
        assert result == expected

    def test_div0(self):
        # arrange
        a = 333
        b = 0
        cal = Calculator()

        # assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)