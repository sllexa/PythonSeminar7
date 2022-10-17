from fractions import Fraction


def format_data(data):
    type_c, f_num, s_num, oper = data
    if type_c == "1":
        f_num = complex(f_num)
        s_num = complex(s_num)
    elif type_c == "2":
        n = f_num
        f_num = Fraction(int(n[:n.index("/")]), int(n[n.index("/")+1:len(n)]))
        n = s_num
        s_num = Fraction(int(n[:n.index("/")]), int(n[n.index("/")+1:len(n)]))
    return (f_num, s_num, oper)