# Здесь методы, проверяющие правильность ввода

# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

import test

symbol = "+, -, *, /, ., (, )"

def assembly_example(stroka:str) -> str:
    '''
    Метод соберет математическон выражение, если оно есть в
    аргументе, при этом отбросив мусор, проверит достаточно ли числовых данных,
    проверит на правильность ввода и корректность записи скобок, выведе результат
    '''
    result = ""
    i = 0
    while i < len(stroka):
        if stroka[i] in ["+", "-", "*", "/", "(", ")", "."]:
            result += stroka[i] + " "
        if stroka[i].isdigit():
            if i != len(stroka) - 1:
                if stroka[i + 1].isdigit():
                    result += stroka[i]
                else:
                    result += stroka[i] + " "
            else:
                result += stroka[i]
        i += 1
   
    result = result.split( )

    number = 0
    skobki_open = 0
    skobki_closed = 0
    snaki = 0
    for i in result:
        if i.isdigit():
            number += 1
        if i == "(":
            skobki_open += 1
        if i == ")":
            skobki_closed += 1
        

    test.assembly_minus_number(result)
    for i in result:
        if i == "+" or i == "-" or i == "*" or i == "/":
            snaki += 1

    if number != snaki + 1:
        print("Недостаточно числовых данных!")
        return
    if number == 0:
        print("Неправильный ввод: нужны числа!")
        return
    if skobki_open != skobki_closed:
        print("Некорректная запись скобок!")
        return

    test.queue(result)


