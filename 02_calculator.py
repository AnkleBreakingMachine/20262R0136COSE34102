def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else "Division by zero"
    return "Invalid operator"

print(calculate(10, 5, "+"))
print(calculate(10, 5, "/"))
