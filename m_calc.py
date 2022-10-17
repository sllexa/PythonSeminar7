
def calculate_data(data):
    f_num, s_num, oper = data
    if oper == "+":
        return summa(f_num, s_num)
    if oper == "-":
        return sub(f_num, s_num)
    if oper == "*":
        return mult(f_num, s_num)
    if (oper == "/") and (s_num != 0):
        return div(f_num, s_num)
    else:
        return "Ошибка! Деление на ноль."


def summa(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b