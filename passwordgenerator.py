#importing Libraries
from tkinter import *
import tkinter.font as font
import random, string
import pyperclip
from tkinter.colorchooser import askcolor


###initialize window
root =Tk()
root.option_add("*Font",("Pixel LCD-7",20,'bold'))
root.geometry("700x700")
frameoption = Frame(root, background="#fd62ca")
root.iconbitmap('Downloads\\password_generator\\password.ico')
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.configure(background="#262335")


#heading
Label(root, text = 'PASSWORD GENERATOR' , font =('8BIT WONDER',25), fg="#fd62ca", background='#262335').pack(padx=20, pady=20)
Label(root, text = '_'*350 , font =('8BIT WONDER',3), fg="#689fe4", background='#689fe4').pack()
Label(root, text = '_'*350 , font =('8BIT WONDER',3), fg="#689fe4", background='#689fe4').pack(side = BOTTOM)
Label(root, text ='เจนและผองเพื่อน', font ='arial 20 bold', background='#262335', fg='#31ffec').pack(side=BOTTOM)
Label(root, text ='EFGPKPGFE', font =('Mushroom Kingdom NBP Regular',30), fg="#fd62ca", background="#262335").pack(side = BOTTOM)

###select password length
Label(root, text ='PASSWORD LENGTH', font =('8BIT WONDER',15), fg="#31ffec", background='#262335').pack(padx=10, pady=10)
pass_len = IntVar()
Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15, font="arial 15 bold").pack(padx=5,pady=5)

var_low = IntVar()
var_up = IntVar()
var_spe = IntVar()
var_num = IntVar()

frameoption.pack(padx=10, pady=10)
Checkbutton(frameoption, text='Upper  ?', variable=var_up, background='#fd62ca', fg="#1914e1").pack(padx=10, pady=5)
Checkbutton(frameoption, text='Lower  ?', variable=var_low, background='#fd62ca', fg="#1914e1").pack(padx=5,pady=5)
Checkbutton(frameoption, text='Special  ?', variable=var_spe, background='#fd62ca', fg="#1914e1").pack(padx=5,pady=5)
Checkbutton(frameoption, text='Number  ?', variable=var_num, background='#fd62ca', fg="#1914e1").pack(padx=5,pady=5)

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
Button(root, text = "GENERATE PASSWORD" , command = Generator, font =('8BIT WONDER',15), fg="#ffffff", background='#689fe4').pack(pady= 10)

Entry(root , textvariable = pass_str, fg="red", font =('Nerko One',20)).pack(pady=10)

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password, font =('8BIT WONDER',15), fg="#ffffff", background='#689fe4').pack(pady=8)

# loop to run program
root.mainloop() 
