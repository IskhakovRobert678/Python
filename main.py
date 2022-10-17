oper_plus = []
oper_minus = []
oper_multi = []
oper_division = []

num1 = None
num2 = None
result = None
on = 1
while on == 1:

    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    sign = input("Введите знак(+, -, *, /): ")

    if num1 == "" or num2 == "" or sign == "":
        print("Зачем ломаешь? води нормально num1 и num2 это цифры, sign это один из знаков (- + - * /)")
        break

    if sign == '+':
        result = int(num1) + int(num2)
        oper = num1 + sign + num2 + "=" + str(result)
        oper_plus.append(oper)
    if sign == '-':
        result = int(num1) - int(num2)
        oper = num1 + sign + num2 + "=" + str(result)
        oper_minus.append(oper)
    if sign == '*':
        result = int(num1) * int(num2)
        oper= num1 + sign + num2 + "=" + str(result)
        oper_multi.append(oper)
    if sign == '/' and int(num2) != 0:
        result = int(num1) / int(num2)
        oper = num1 + sign + num2 + "=" + str(result)
        oper_division.append(oper)

    print(f"\n{num1}{sign}{num2}={str(result)}")

    print('+', oper_plus)
    print('-', oper_minus)
    print('*', oper_multi)
    print('/', oper_division)