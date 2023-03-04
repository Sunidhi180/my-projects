print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1 = int(input("enter the value1:-"))
num2 = int(input("enter the value2:-"))
opr = input("enter the opr...(+,-,*,/)")
if opr == "+":
    print(num1 + num2)
if opr == "-":
    print(num1 - num2)
if opr == "*":
    print(num1 * num2)
if opr == "/":
    print(num1 / num2)
if opr != "+" and opr != "-" and opr != "*" and opr != "/":
    print("invalid opr...")