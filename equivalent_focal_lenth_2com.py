from tkinter import * # импортируем библиотеку
import math

# создаем окно с названием и заданными размерами
root = Tk()
root.title("Еквівалентна оптична сила та фокусна відстань (2 компонента)")
root.geometry("600x150")
root.update()

 # поле для ввода фокусного расстояния первого компонента f1
f1 = Entry(root, width = 50)
f1.grid(row=0, column=1)

# поле для ввода фокусного расстояния первого компонента f2
f2 = Entry(root, width = 50)
f2.grid(row=1, column=1)

# поле для ввода расстояния между линзами
d = Entry(root, width = 50)
d.grid(row=2, column=1)


# поле для вывода результатов расчета эквивалентной оптической силы Ф
output = Text(root, bg="#28b", fg="#ccc", font=("Arial 11"), width=30, height=1)
output.grid(row=3, column=1)
output_f = Text(root, bg="#28b", fg="#ccc", font="Arial 11", width=30, height=1)
output_f.grid(row=4, column=1)


# создаем функцию для расчета эквивалентной оптической силы и фокусного расстояния, в случае деления на ноль будет выдавать ошибку
def calc_result(f1, f2, d):
    try:
        F1 = 1 / (f1 * 0.001)
        F2 = 1 / (f2 * 0.001)
        calc_Fekv = F1 + F2 - F1 * F2 * d * 0.001
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
        d_value = float(d.get())
        res1, res2 = calc_result(f1_value, f2_value, d_value)
        inserter(res1, res2)
    except ValueError:
        inserter ("ERROR", "ERROR")


# создаем строки указатели вводимых данных и полученных результатов
label_f1_text = Label(text="Фокусна відстань першого компонента, [мм]")
label_f2_text = Label(text="Фокусна відстань другого компонента, [мм]")
label_d_text = Label(text="Відстань між компонентами, [мм]")
label_F_ekv_text = Label(text="Еквівалентна оптична сила, Ф [дптр]")
label_f_ekv_text = Label(text="Еквівалента фокусна відстань, f` [мм]")

# создаем кнопку для запуска расчета
button_calc = Button(root, text="Розрахувати", command=handler).grid(row=6, column=1, padx=(10,0))

# размещаем строки и кнопки в окне
label_f1_text.grid(row=0, column=0, sticky=W)
label_f2_text.grid(row=1, column=0, sticky=W)
label_d_text.grid(row=2, column=0, sticky=W)
label_F_ekv_text.grid(row=3, column=0, sticky=W)
label_f_ekv_text.grid(row=4, column=0, sticky=W)
# button_clear.grid(row=1, column=3)

# Включаем постоянную отрисовку окна
root.mainloop()
