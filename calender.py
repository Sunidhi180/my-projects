from tkinter import *
import calendar

text = calendar.calendar(2022)

root = Tk()
root.geometry("600x700")
root.title("CALENDER")
label1 = Label(root, text="CALENDER", bg="blue", font=("times", 28, "bold"))
label1.grid(row=1, column=1)
root.config(background="red")
l1 = Label(root, text=text, font="consolas 10 bold")
l1.grid(row=2, column=1, padx=20)
root.mainloop()

