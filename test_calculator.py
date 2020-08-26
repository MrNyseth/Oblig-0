from calculator import *
import pytest
# Test add function in calculator.py: 1 + 2 = 4
def test_add_excercise_1():
    assert add(1, 2) == 4

# Test add function in calculator.py: 0.1 + 0.2 = 0.3
def test_add_float_excercise_2():
    tol = 1e-12
    assert add(0.1, 0.2) - 0.3 < tol

# Test add function in calculator.py for adding strings:
def test_str_excercise_3():
    assert add("Hello ", "world") == "Hello world"

# Test factorial function in calculator.py against math.factorial function
def test_factorial_excercise_4():
    tol = 1e-12
    n = 43
    assert factorial(n) - math.factorial(n) < tol

# Test sin function in calculator.py: sin(pi/2) = 1
def test_sin_excercise_4():
    tol = 1e-12
    assert sin(np.pi/2) - 1 < tol

# Test divide function in calculator: 2/2 = 1
def test_divide_excercise_4():
    tol = 1e-12
    assert divide(1, 10) - 0.1 < tol

# Test multiply function in calculator: 3 * 4 = 12
def test_multiply_excercise_4():
    assert multiply(3, 4) == 12

# Test pow_eul function in calculator against numpy.exp function
def test_pow_eul_excercise_4():
    tol = 1e-12
    assert pow_eul(7) - np.exp(7) < tol

# Test add function does not allow string to be added to float or int
def test_add_types_exercise_5():
    with pytest.raises(TypeError):
        add("to", 2)

# Test divide function for divide by zero
def test_divide_by_zero_exercise_5():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

# All test below tests same functions as above but witt several inputs
@pytest.mark.parametrize("x, y, z", [(0, 0, 0), (1, 1, 2), (2, 4, 6), (3, 9, 12)])
def test_add_excercise_6(x, y, z):
    assert add(x, y) == z


@pytest.mark.parametrize("x, y, z", [(0.1, 0.2, 0.3), (0.1, 0.1, 0.2), (0.2, 0.4, 0.6), (1.3, 1.9, 3.2)])
def test_add_float_excercise_6(x, y, z):
    tol = 1e-12
    assert add(x, y) - z < tol


@pytest.mark.parametrize("x, y, z", [("Hello ", "world", "Hello world"), ("I ", "am", "I am"), ("Bat", "man", "Batman")])
def test_str_excercise_6(x, y, z):
    assert add(x, y) == z


@pytest.mark.parametrize("x", [2, 4, 8, 15, 42])
def test_factorial_excercise_6(x):
    tol = 1e-12
    assert factorial(x) - math.factorial(x) < tol


@pytest.mark.parametrize("x", [np.pi, np.pi/2, np.pi/4, np.pi/6])
def test_sin_excercise_6(x):
    tol = 1e-12
    assert sin(x) - math.sin(x) < tol


@pytest.mark.parametrize("x, y, z", [(3, 2, 1.5), (10, 5, 2), (20, 4, 5), (1, 10, 0.1)])
def test_divide_excercise_6(x, y, z):
    tol = 1e-12
    assert divide(x, y) - z < tol


@pytest.mark.parametrize("x, y, z", [(5, 3, 15), (6, 7, 42), (13, 22, 286), (0, 2, 0), (1, 1, 1)])
def test_multiply_excercise_6(x, y, z):
    assert multiply(x, y) == z


@pytest.mark.parametrize("x", [3, 8, 9, 12, 35])
def test_pow_eul_excercise_6(x):
    tol = 1e-12
    assert pow_eul(x) - np.exp(x) < tol


@pytest.mark.parametrize("x, y", [("Word", 4), (3.2, "Number"), ("float", 3), (3, "int")])
def test_add_types_exercise_6(x, y):
    with pytest.raises(TypeError):
        add(x, y)


@pytest.mark.parametrize("x, y", [(3, 0), (10, 0), (5, 0), (1931, 0)])
def test_divide_by_zero_exercise_6(x, y):
    with pytest.raises(ZeroDivisionError):
        divide(x, y)
