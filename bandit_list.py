import tkinter
import random

# правила игры
# один ход - 10 рублей
# один выигрыш - 300 рублей

tratim = 0
score = 0

def new_picture():
    k = random.randint(0, 7)
    list_pic = [pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8]
    return list_pic[k]

def click():
    global tratim, score
    button1.config(image=new_picture())
    button2.config(image=new_picture())
    button3.config(image=new_picture())
    if button1.cget("image") == button2.cget("image") and button1.cget("image") == button3.cget("image"):
        score = score + 300
        label_win.config(text=str(score))
    tratim = tratim + 10
    label_tratim.config(text=str(tratim))

win = tkinter.Tk()
win.geometry("400x400")
win.title("Однорукий бандит")

# загрузить картинки
pic1 = tkinter.PhotoImage(file="seven.png")
pic2 = tkinter.PhotoImage(file="almaz.png")
pic3 = tkinter.PhotoImage(file="limon.png")
pic4 = tkinter.PhotoImage(file="hear.png")
pic5 = tkinter.PhotoImage(file="happy.png")
pic6 = tkinter.PhotoImage(file="sherry.png")
pic7 = tkinter.PhotoImage(file="ding.png")
pic8 = tkinter.PhotoImage(file="melon.png")

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