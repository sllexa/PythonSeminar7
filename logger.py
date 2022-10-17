from datetime import datetime as dt

def write_result(data, result):
    f_num, s_num, oper = data
    str_data = f"{f_num} {oper} {s_num}"
    time_c = dt.now().strftime("%d.%m.%Y %H:%M")
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f"{time_c}; операция: {str_data} результат: {result}\n")

def write_log(text):
    time_c = dt.now().strftime("%d.%m.%Y %H:%M")
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f"{time_c}; {text}\n")
