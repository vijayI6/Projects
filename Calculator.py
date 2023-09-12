# calculator using eval function
exp = eval(input("Enter a expression:"))
print(exp)

# making calculator using if-elif-else statements

num1 = float(input("Enter number1:"))
op = input("Enter a operand:")
num2 = float(input("Enter number2:"))
if op == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
elif op == '**':
    print(f"{num1} ** {num2} = {num1 ** num2}")
elif op == '//':
    print(f"{num1} // {num2} = {num1 // num2}")
else:
    print("Enter basic operators ")
