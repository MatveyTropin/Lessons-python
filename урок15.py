import tkinter as t
import tkinter.filedialog as tkf
def dark():
    textarea.config(bg="black",fg="white",insertbackground="white")
def violet():
    textarea.config(bg="violet",fg="green",insertbackground="green")
def yellow():
    textarea.config(bg="yellow",fg="black",insertbackground="Black")
def white():
    textarea.config(bg="white",fg="black",insertbackground="Black")
def save_file():
    global filename
    if filename=="":
        save_as()
    else:
        with open(filename,mode="w") as file:
            text=textarea.get(1.0,"end")
            file.write(text)
def save_as():
    global filename
    filename=tkf.asksaveasfilename()
    save_file()


def open_file():
    global filename
    filename=tkf.askopenfilename()
    with open (filename,encoding="UTF-8") as file:
        text=file.read()
        textarea.delete(1.0,"end")
        textarea.insert(1.0,text)
        window.title(filename)
def new_file():
    global filename
    filename=""
    window.title("notes")
    textarea.delete(1.0,"end")
window=t.Tk()
window.geometry("800x700")
window.title("notes")
logo=t.PhotoImage(file="note.png")
window.iconphoto(True,logo)
textarea=t.Text()
textarea.config(bg="dark blue",fg="white")
textarea.place(x=0,y=0,relwidth=1,relheight=1)
#Main menu
main_menu=t.Menu()
window.config(menu=main_menu)
#Icons
new_file_icon=t.PhotoImage(file="new_file.gif")
open_file_icon=t.PhotoImage(file="open_file.gif")
save_file_icon=t.PhotoImage(file="save_file.gif")
dark_icon=t.PhotoImage(file="night-mode.png")
white_icon=t.PhotoImage(file="night-light.png")
yellow_icon=t.PhotoImage(file="brightness.png")
violet_icon=t.PhotoImage(file="violet.png")

#File menu
file_menu=t.Menu(tearoff=0)
file_menu.add_command(label="New file",image=new_file_icon,compound="left",command=new_file)
file_menu.add_command(label="Open file",image=open_file_icon,compound="left",command=open_file)
file_menu.add_command(label="Save file",image=save_file_icon,compound="left",command=save_file)
file_menu.add_command(label="Save as...",image=save_file_icon,compound="left",command=save_as)
file_menu.add_command(label="Exit")
main_menu.add_cascade(menu=file_menu,label="File")
#theme_menu
theme_menu=t.Menu(tearoff=0)
theme_menu.add_command(label="dark mode",command=dark,image=dark_icon,compound="left")
main_menu.add_cascade(menu=theme_menu,label="Themes")
theme_menu.add_command(label="light_mode",command=white,image=white_icon,compound="left")
theme_menu.add_command(label="yellow_mode",command=yellow,image=yellow_icon,compound="left")
theme_menu.add_command(label="violet_mode",command=violet,image=violet_icon,compound="left")


filename=""



window.mainloop()
