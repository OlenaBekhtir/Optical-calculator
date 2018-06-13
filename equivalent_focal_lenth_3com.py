from tkinter import * # импортируем библиотеку
import math

# создаем окно с названием и заданными размерами
root2 = Tk()
root2.title("Еквівалентна оптична сила та фокусна відстань (3 компонента)")
root2.geometry("600x180")
root2.update()

 # поле для ввода фокусного расстояния первого компонента f1
f1 = Entry(root2, width = 50)
f1.grid(row=0, column=1)

# поле для ввода фокусного расстояния первого компонента f2
f2 = Entry(root2, width = 50)
f2.grid(row=1, column=1)

# поле для ввода фокусного расстояния первого компонента f3
f3 = Entry(root2, width = 50)
f3.grid(row=2, column=1)

# поле для ввода первого расстояния между линзами d1
d1 = Entry(root2, width = 50)
d1.grid(row=3, column=1)

# поле для ввода второго расстояния между линзами d2
d2 = Entry(root2, width = 50)
d2.grid(row=4, column=1)


# поле для вывода результатов расчета эквивалентной оптической силы Ф и фокусного расстояния
output = Text(root2, bg="#28b", fg="#ccc", font=("Arial 11"), width=30, height=1)
output.grid(row=5, column=1)
output_f = Text(root2, bg="#28b", fg="#ccc", font="Arial 11", width=30, height=1)
output_f.grid(row=6, column=1)


# создаем функцию для расчета эквивалентной оптической силы и фокусного расстояния, в случае деления на ноль будет выдавать ошибку
def calc_result(f1, f2, f3, d1, d2):
    try:
        F1 = 1 / (f1 * 0.001)
        F2 = 1 / (f2 * 0.001)
        F3 = 1 / (f3 * 0.001)
        calc_Fekv = F1 + F2 + F3 - (F2 + F3) * F1 * d1 * 0.001  - (F1 + F2 - F1 * F2 * d1 * 0.001) * F3 * d2 * 0.001
        calc_focal_lenth = 1000 / calc_Fekv
        return calc_Fekv, calc_focal_lenth

    except ZeroDivisionError:
        output.delete("0.0", "end")
        output.insert("0.0", "ERROR")
        output_f.delete("0.0", "end")
        output_f.insert("0.0", "ERROR")


# Функция для вставки информации, очищает поле ввода данных и вставляет туда введенное число
def inserter(value, f_length):
    output.delete("0.0", "end")
    output.insert("0.0", value)
    output_f.delete("0.0", "end")
    output_f.insert("0.0", f_length)


# Функция обработки введенных данных
def handler():
    try:
        f1_value = float(f1.get())
        f2_value = float(f2.get())
        f3_value = float(f3.get())
        d1_value = float(d1.get())
        d2_value = float(d2.get())
        res1, res2 = calc_result(f1_value, f2_value, f3_value, d1_value, d2_value)
        inserter(res1, res2)
    except ValueError:
        inserter ("ERROR", "ERROR")


# создаем строки указатели вводимых данных и полученных результатов
label_f1_text = Label(root2, text="Фокусна відстань першого компонента, [мм]")
label_f2_text = Label(root2, text="Фокусна відстань другого компонента, [мм]")
label_f3_text = Label(root2, text="Фокусна відстань третього компонента, [мм]")
label_d1_text = Label(root2, text="Відстань між першим та другим компонентами, [мм]")
label_d2_text = Label(root2, text="Відстань між другим та третім компонентами, [мм]")
label_F_ekv_text = Label(root2, text="Еквівалентна оптична сила, Ф [дптр]")
label_f_ekv_text = Label(root2, text="Еквівалента фокусна відстань, f` [мм]")

# создаем кнопку для запуска расчета
button_calc = Button(root2, text="Розрахувати", command=handler).grid(row=7, column=1, padx=(10,0))

# размещаем строки и кнопки в окне
label_f1_text.grid(row=0, column=0, sticky=W)
label_f2_text.grid(row=1, column=0, sticky=W)
label_f3_text.grid(row=2, column=0, sticky=W)
label_d1_text.grid(row=3, column=0, sticky=W)
label_d2_text.grid(row=4, column=0, sticky=W)
label_F_ekv_text.grid(row=5, column=0, sticky=W)
label_f_ekv_text.grid(row=6, column=0, sticky=W)
# button_clear.grid(row=1, column=3)

# Включаем постоянную отрисовку окна
root2.mainloop()
