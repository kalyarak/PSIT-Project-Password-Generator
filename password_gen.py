#importing Libraries
from tkinter import *
import random, string
import pyperclip

###initialize window
root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.configure(background='#F6B5C3')

#heading
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='เจนและผองเพื่อน', font ='arial 15 bold', background='#F6B5C3').pack(side = BOTTOM)

###select password length
Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

var_low = IntVar()
var_up = IntVar()
var_spe = IntVar()
var_num = IntVar()

Checkbutton(root, text='Upper?', variable=var_low, font='arial 10 bold').pack()
Checkbutton(root, text='Lower?', variable=var_up, font='arial 10 bold').pack()
Checkbutton(root, text='Special?', variable=var_spe, font='arial 10 bold').pack()


Checkbutton(root, text='Number?', variable=var_num, font='arial 10 bold').pack()

#####define function
pass_str = StringVar()

def Generator():
    low_letter = string.ascii_lowercase*var_low.get()
    up_letter = string.ascii_uppercase*var_up.get()
    special = '$#@!%^&*()'*var_spe.get()
    number = string.digits*var_num.get()
    all_char = list(low_letter+up_letter+special+number)
    password = random.choices(all_char, k=pass_len.get())
    password = ''.join(password)
    pass_str.set(password)

###button
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

# loop to run program
root.mainloop()
