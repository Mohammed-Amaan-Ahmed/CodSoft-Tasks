def calculate():
  num1 = float(input("Enter the first number: "))
  operator = input("Enter the operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))
  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
    else:
      result = num1 / num2
  else:
    print("Invalid operator")
  print("The result is:", result)
calculate()
