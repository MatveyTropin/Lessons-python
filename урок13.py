import tkinter
def plus():
    number1=entry1.get()
    number2=entry2.get()
    answer=int(number1)+int(number2)
    entry3.delete(0,"end")
    entry3.insert(0,answer)
def minus():
    number1=entry1.get()
    number2=entry2.get()
    answer=int(number1)-int(number2)
    entry3.delete(0,"end")
    entry3.insert(0,answer)
def mult():
    number1=entry1.get()
    number2=entry2.get()
    answer=int(number1)*int(number2)
    entry3.delete(0,"end")
    entry3.insert(0,answer)
def div():
    number1=entry1.get()
    number2=entry2.get()
    if number2=="0":
        print("На ноль делить нельзя!")
    else:
        answer=int(number1)/int(number2)
        entry3.delete(0,"end")
        entry3.insert(0,answer)
def clear():
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry3.delete(0,"end")
    entry1.focus_set()
window=tkinter.Tk()
window.geometry("400x600")
window.title("My Calculator")
window.config(bg="orange")
font=("arial",20)
pius_btn=tkinter.Button(text="+",bg="red",width=3,height=3,font=font,command=plus)
pius_btn.place(x=50,y=370)
minus_btn=tkinter.Button(text="-",bg="red",width=3,height=3,font=font,command=minus)
minus_btn.place(x=125,y=370)
mult_btn=tkinter.Button(text="*",bg="#20bf6b",width=3,height=3,font=font,command=mult)
mult_btn.place(x=200,y=370)
div_btn=tkinter.Button(text=":",bg="#20bf6b",width=3,height=3,font=font,command=div)
div_btn.place(x=275,y=370)
entry1=tkinter.Entry(font=font)
entry1.place(x=50,y=100)
entry2=tkinter.Entry(font=font)
entry2.place(x=50,y=300)
entry3=tkinter.Entry(font=font)
entry3.place(x=50,y=550)
label1=tkinter.Label(text="first number",font=font)
label1.place(x=50,y=60)
label2=tkinter.Label(text="second number",font=font)
label2.place(x=50,y=260)
label3=tkinter.Label(text="answer",font=font)
label3.place(x=50,y=510)
clear=tkinter.Button(text="Clear",font=font,command=clear)
clear.place(x=50,y=160)






window.mainloop()
