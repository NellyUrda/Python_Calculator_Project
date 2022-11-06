import tkinter.messagebox
from tkinter import *
from operations import Operacions

operations = Operacions()


# input the values of two numbers and choose an operation
# (addition, subtraction, multiplication, division )
def operacion():
    try:
        current_selection = list_box.get(list_box.curselection())
        if current_selection == "addition":
            result_entrybox.delete(0, END)
            nr1 = float(nr1_entrybox.get())
            nr2 = float(nr2_entrybox.get())
            result = float(operations.addition(nr1, nr2))
            result_entrybox.insert(0, str(result))
        elif current_selection == "subtraction":
            result_entrybox.delete(0, END)
            nr1 = float(nr1_entrybox.get())
            nr2 = float(nr2_entrybox.get())
            result = float(operations.substraction(nr1, nr2))
            result_entrybox.insert(0, str(result))  # adauga text in entrybox
        elif current_selection == "multiplication":
            result_entrybox.delete(0, END)
            nr1 = float(nr1_entrybox.get())
            nr2 = float(nr2_entrybox.get())
            result = float(operations.multiplication(nr1, nr2))
            result_entrybox.insert(0, str(result))  # adauga text in entrybox
        elif current_selection == "division":
            result_entrybox.delete(0, END)
            nr1 = float(nr1_entrybox.get())
            nr2 = float(nr2_entrybox.get())

            try:
                result = float(operations.division(nr1, nr2))
                result_entrybox.insert(0, str(result))
            except Exception:
                tkinter.messagebox.showinfo(message="Cannot divide by zero. Enter another number! ")

    except Exception:
        tkinter.messagebox.showinfo(message="Enter a number!!!")


# GUI for calculator page
calculator_window = Tk()

calculator_window.geometry("480x480")
calculator_window.config(background="#6a606e")  # culoarea ferestrei

title_label = Label(calculator_window,
                    text="Calculator",
                    font=("Ariel", 20, "bold"),
                    fg="#b9d613",
                    bg="black")
title_label.place(x=130, y=10, height=40, width=170)

first_number_label = Label(calculator_window,
                           text="First number",
                           font=("Ariel", 12, "bold"),
                           fg="black",
                           bg="#6a606e")
first_number_label.place(x=45, y=70, height=30, width=140)

nr1_entrybox = Entry(calculator_window, font=("Ariel", 12))
nr1_entrybox.place(x=230, y=70, height=30, width=110)

second_number_label = Label(calculator_window,
                            text="Second number",
                            font=("Ariel", 12, "bold"),
                            fg="black",
                            bg="#6a606e")
second_number_label.place(x=50, y=150, height=30, width=140)

nr2_entrybox = Entry(calculator_window, font=("Ariel", 12))
nr2_entrybox.place(x=230, y=150, height=30, width=110)

operation_label = Label(calculator_window,
                        text="Operation",
                        font=("Ariel", 12, "bold"),
                        fg="black",
                        bg="#6a606e")
operation_label.place(x=50, y=230, height=30, width=90)

list_box = Listbox(calculator_window,
                   bg="white",
                   font=("Ariel", 12, "bold"),
                   selectbackground="#b9d613")  # culoarea scrisului cand e selectat
list_box.place(x=230, y=210, width=110)
list_box.insert(1, "addition")
list_box.insert(2, "subtraction")
list_box.insert(3, "multiplication")
list_box.insert(4, "division")
list_box.config(height=list_box.size())  # lungimea listei=nr de elemente adaugate

result_label = Label(calculator_window,
                     text="Result",
                     font=("Ariel", 12, "bold"),
                     fg="black",
                     bg="#6a606e")
result_label.place(x=45, y=360, height=30, width=90)

result_entrybox = Entry(calculator_window, font=("Ariel", 12))
result_entrybox.place(x=230, y=360, height=30, width=110)

calculate_button = Button(calculator_window,
                          text="Calculate",
                          font=("Ariel", 12, "bold"),
                          fg="#b9d613",
                          bg="#1b1a1c",
                          activebackground="#1b1a1c",
                          activeforeground="#b9d613",
                          command=operacion)
calculate_button.place(x=160, y=420, height=40, width=100)

calculator_window.mainloop()
