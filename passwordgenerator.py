#importing Libraries
from tkinter import *
import tkinter.font as font
import random, string
import pyperclip
from tkinter.colorchooser import askcolor
from PIL import ImageTk

def getColor():
    color = askcolor()
    return color[-1]

def storecolor():
    store = getColor()
    return store

valu = storecolor()

###initialize window
root =Tk()
root.option_add("*Font",("Atari Classic",15))
root.configure(background=getColor())
# f1 = Frame(root, bg="green")
# f1.grid(row=1, column=0)
root.geometry("650x650")
root.resizable(0,0)
root.title("PASSWORD GENERATOR") 
# root.wm_attributes("-alpha",1)




Button(text='Color', command=getColor)

#heading
Label(root, text = 'PASSWORD GENERATOR' , font =('Arista 2.0 Alternate Regular',30),background=valu).pack(padx=20, pady=20)
Label(root, text ='เจนและผองเพื่อน', font ='arial 20 bold', background=valu).pack(side = BOTTOM)
Label(root, text ='EFGPKPGFE', font =('Mushroom Kingdom NBP Regular',30), background=valu).pack(side = BOTTOM)

###select password length
Label(root, text = 'PASSWORD LENGTH').pack(padx=10, pady=10)
pass_len = IntVar()
Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15, font="arial 15 bold").pack(padx=5,pady=5)

var_low = IntVar()
var_up = IntVar()
var_spe = IntVar()
var_num = IntVar()

Checkbutton(root, text='Upper?', variable=var_up).pack(padx=10, pady=5)
Checkbutton(root, text='Lower?', variable=var_low).pack(padx=5,pady=5)
Checkbutton(root, text='Special?', variable=var_spe).pack(padx=5,pady=5)
Checkbutton(root, text='Number?', variable=var_num).pack(padx=5,pady=5)

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
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 10)

Entry(root , textvariable = pass_str, font="arial 15 bold", fg="red").pack()

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=8)

# loop to run program
root.mainloop() 