def function_1(x, y):
    return x + y
def function_2(x, y):
    return x - y
def function_3(x, y):
    return x * y
def function_4(x, y):
    return x / y
print("Выберите операцию")
print("a. Сложение")
print("b. Вычитание")
print("c. Умножение")
print("d. Деление")
while True:
    choice = input("Выберите операцию (a/ b/ c/ d): ")
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))
    if choice == 'a':
        print(num_1, " + ", num_2, " = ", function_1(num_1, num_2))
    elif choice == 'b':
        print(num_1, " - ", num_2, " = ", function_2(num_1, num_2))
    elif choice == 'c':
        print(num_1, " * ", num_2, " = ", function_3(num_1, num_2))
    elif choice == 'd':
        if num_2==0:
            break
        print(num_1, " / ", num_2, " = ", function_4(num_1, num_2))
