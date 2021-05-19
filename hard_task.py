def comp(num1, num2):
    if (type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
        if num1 > num2:
            return num1
        elif num1 < num2:
            return num2
        else:
            return num1
    else:
        raise ValueError("Некоректные числа для сравнения")

def edit(num, day, k):
    while day:
        if (type (day) == int) and (type(num) == int or type(num) == float) and (type(k) == int or type(k) == float):
            num *= k
            day -= 1
            time(datetime.datetime.today (),"Была вызвана функция" )
            return num
        else:
            raise TypeError


try:
    print(edit())
except TypeError:
    print("Вводить только числа")
except ValueError:
    print("Некорректные числа")





import datetime
def time (date, messege):
    with open ('text.txt', 'a') as a:
        return a.write(date, messege)







