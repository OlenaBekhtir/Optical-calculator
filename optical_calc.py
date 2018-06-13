from tkinter import * #импортируем библиотеку

# создаем окно с названием и заданными размерами
root = Tk()
root.title("Оптичний калькулятор")
root.geometry("250x100")
root.update()

# функция, которая вызывает окно расчета двухкомпонентной оптической системы
def calc_2com():
    import equivalent_focal_lenth_2com

# функция, которая вызывает окна расчета трехкомпонентной оптической системы
def calc_3com():
    import equivalent_focal_lenth_3com

# Создаем кнопки перехода на нужный пользователю расчет оптики
button_2com = Button(text="Розрахунок Ф_ekv та f`_ekv (2 компоненти)", command=calc_2com).grid(row=0, column=3)
button_3com = Button(text="Розрахунок Ф_ekv та f`_ekv (3 компоненти)", command=calc_3com).grid(row=1, column=3)

# Включаем постоянную отрисовку окна
root.mainloop()
