# mathematical operations functions are defined here
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Error! Division by zero"
  return a / b

def main():
  print("We do maths in here!")
  print("Addition of 5 and 3 is", add(5, 3))
  print("Subtraction of 5 and 3 is", subtract(5, 3))
  print("Multiplication of 5 and 3 is", multiply(5, 3))
  print("Division of 5 and 3 is", divide(5, 3))
  
if __name__ == "__main__":
  main()
