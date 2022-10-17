# **Задача:** Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.
import console_ui as ui
import data_transform as dt
from m_calc import calculate_data as cd
import logger as log

def run_calc():
    log.write_log("Запуск программы")
    while True:
        print()
        print(ui.welcome)
        ui.print_menu(ui.list_menu)

        t_calc = ui.ask_calc_type()
        data = dt.format_data(ui.input_data(t_calc))
        result = cd(data)
        ui.print_result(data, result)
        log.write_result(data, result)


run_calc()