from logger import write_log as wl

welcome = "Добро пожаловать в калькулятор!\nВыберите режим работы калькулятора:"
mes_actions = "Выберите операцию:"
list_menu = ["1. Комплексные числа", "2. Рациональные числа", "3. Выход"]
list_sub_menu = ["1. Сложение", "2. Вычитание", "3. Умножение", "4. Деление"]

def print_menu(lst_menu):
    print("-------------------------------------")
    for i in range(len(lst_menu)):
        print(lst_menu[i])
    print("-------------------------------------")

def ask_calc_type():
    value = input(">>> ")
    if value == "3": 
        wl("Выход из программы")
        exit()
    while not (value == "1" or value == "2"):
        print("Неправильный ввод \nОжидалось: 1 или 2")
        value = input(">>> ")
    return value


def ask_sub_menu():
    value = input(">>> ")
    while not (value == "1" or value == "2" or value == "3" or  value == "4"):
        print("Неправильный выбор операции!\nОжидалось: 1 или 2 или 3 или 4")
        value = input(">>> ")
    if value == "1": action = "+"
    if value == "2": action = "-"
    if value == "3": action = "*"
    if value == "4": action = "/"     
    return action

def input_data(type_c):
    if type_c == "1":
        f_num = input("Введите первое число (формат: '2+3j'): ")
        s_num = input("Введите второе число (формат: '2+3j'): ")
    elif type_c == "2":
        f_num = input("Введите первое число (формат: '2/10'): ")
        s_num = input("Введите второе число (формат: '2/10'): ")
    print(mes_actions)
    print_menu(list_sub_menu)
    oper = ask_sub_menu()
    return (type_c, f_num, s_num, oper)

def print_result(data, result):
    f_num, s_num, oper = data
    str_data = f"{f_num} {oper} {s_num}"
    print(f"{str_data} = {result}")