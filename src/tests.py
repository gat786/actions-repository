import main

def test_addition():
    assert main.add(5, 3) == 8
    
def test_subtraction():
    assert main.subtract(5, 3) == 2
    
def test_multiplication():
    assert main.multiply(5, 3) == 15
    
def test_division():
    assert main.divide(5, 3) == 5/3
    assert main.divide(5, 0) == "Error! Division by zero"
