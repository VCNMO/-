import tkinter
import random

# правила игры
# один ход - 10 рублей
# один выигрыш - 300 рублей

tratim = 0
win = 0

def new_picture():
    k = random.randint(1, 3)
    if k == 1:
        return pic1
    elif k == 2:
        return pic2
    else:
        return pic3

def click():
    global tratim
    button1.config(image=new_picture())
    button2.config(image=new_picture())
    button3.config(image=new_picture())
    print(button1.image == button2.image)
    tratim = tratim + 10
    label_tratim.config(text=str(tratim))

win = tkinter.Tk()
win.geometry("400x400")
win.title("Однорукий бандит")

# загрузить картинки
pic1 = tkinter.PhotoImage(file="seven.png")
pic2 = tkinter.PhotoImage(file="almaz.png")
pic3 = tkinter.PhotoImage(file="limon.png")

#сделать три кнопки
button1 = tkinter.Button(image=pic1)
button1.place(x=10, y=10)

button2 = tkinter.Button(image=pic2)
button2.place(x=100, y=10)

button3 = tkinter.Button(image=pic3)
button3.place(x=200, y=10)

button_push = tkinter.Button(text="дергай ручку", command=click)
button_push.place(x=100, y=100)


label1 = tkinter.Label(text="ВСЕГО ПОТРАЧЕНО РУБЛЕЙ")
label1.place(x=50, y=180)

label_tratim = tkinter.Label(text="0")
label_tratim.place(x=50, y=200)

label2 = tkinter.Label(text="ВСЕГО ВЫИГРАНО РУБЛЕЙ")
label2.place(x=50, y=280)

label_win = tkinter.Label(text="0")
label_win.place(x=50, y=300)

win.mainloop()