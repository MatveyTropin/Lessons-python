import tkinter
import random
def reset_mode_colors():
    easy_btn.config(bg="green")
    hard_btn.config(bg="yellow")
    unreal_btn.config(bg="red")
def easy():
    global level
    level="easy"
    reset_mode_colors()
    easy_btn.config(bg="purple")
def hard():
    global level
    level="hard"
    reset_mode_colors()
    hard_btn.config(bg="purple")
def unreal():
    global level
    level="unreal"
    reset_mode_colors()
    unreal_btn.config(bg="purple")
def reset_colors():
    addition_btn.config(bg="blue")
    subtraction_btn.config(bg="blue")
    division_btn.config(bg="blue")
    multiplication_btn.config(bg="blue")
def get_numbers():
    if level=="easy":
        min=1
        max=9
    elif level=="hard":
        min=10
        max=99
    else:
        min=100
        max=999
    number1=random.randint(min,max)
    number2=random.randint(min,max)
    return number1,number2
def addition():
    global answer
    reset_colors()
    addition_btn.config(bg="purple")
    number1,number2=get_numbers()
    question_text.config(text=f"{number1} + {number2} = ?")
    answer=number1 + number2
def subtraction():
    global answer
    reset_colors()
    subtraction_btn.config(bg="purple")
    number1,number2=get_numbers()
    question_text.config(text=f"{number1} - {number2} = ?")
    answer=number1 - number2
def division():
    global answer
    reset_colors()
    division_btn.config(bg="purple")
    number1,number2=get_numbers()
    question_text.config(text=f"{number1} / {number2} = ?")
    answer=number1 / number2
def multiplication():
    global answer
    reset_colors()
    multiplication_btn.config(bg="purple")
    number1,number2=get_numbers()
    question_text.config(text=f"{number1} * {number2} = ?")
    answer=number1 * number2
def check_answer():
    global right
    user_answer=float(answer_entry.get())
    if user_answer==answer:
        right = right + 1
        right_text.config(text=f"Right: {right}")

    else:
        print(f"Wrong, the right answer is {answer}")
window=tkinter.Tk()
window.geometry("800x500")
window.title("Math test")
window.config(bg="#19be84")
addition_btn=tkinter.Button(text="Addition",bg="purple",width=11,height=4,command=addition)
addition_btn.place(x=100,y=200)
subtraction_btn=tkinter.Button(text="Subtraction",bg="Blue",width=11,height=4,command=subtraction)
subtraction_btn.place(x=260,y=200)
multiplication_btn=tkinter.Button(text="Multiplication",bg="Blue",width=11,height=4,command=multiplication)
multiplication_btn.place(x=420,y=200)
division_btn=tkinter.Button(text="Division",bg="Blue",width=11,height=4,command=division)
division_btn.place(x=580,y=200)
easy_btn=tkinter.Button(text="easy",bg="purple",width=8,height=3,command=easy)
easy_btn.place(x=100,y=50)
hard_btn=tkinter.Button(text="hard",bg="yellow",width=8,height=3,command=hard)
hard_btn.place(x=190,y=50)
unreal_btn=tkinter.Button(text="unreal",bg="red",width=8,height=3,command=unreal)
unreal_btn.place(x=280,y=50)
question_text=tkinter.Label(text="7+8=?",font=("Haettenschweiler",30))
question_text.place(x=300,y=350)
answer_entry=tkinter.Entry(font=("Haettenschweiler",30))
answer_entry.place(x=220,y=420)
answer_Button=tkinter.Button(text="Answer",bg="Blue",width=8,height=2,command=check_answer)
answer_Button.place(x=550,y=420)
right_text=tkinter.Label(text="Right:0",font=("Haettenschweiler",30))
right_text.place(x=500,y=50)
wrong_text=tkinter.Label(text="Wrong:0",font=("Haettenschweiler",30))
wrong_text.place(x=650,y=50)
right=0
wrong=0
answer=15
level="easy"
window.mainloop()
Hello

