#importing Libraries
from tkinter import *
import tkinter.font as font
import random, string
import pyperclip
from tkinter.colorchooser import askcolor
import tkinter.ttk


###initialize window
root =Tk()
root.option_add("*Font",("Pixel LCD-7",15,'bold'))
root.geometry("720x780")

#header frame
frametop = Frame(root, background="#262335")
frametop.grid(row=0, column=0, columnspan=5)

#random password frame
frameleft1 = Frame(root, background="#262335")
frameleft1.grid(row=1, column=0)

frameoption = Frame(root, background="#fd62ca")
frameoption.grid(row=2, column=0)

frameleft2 = Frame(root, background="#262335")
frameleft2.grid(row=3, column=0)

# line canvas frame
framemid = Frame(root,background="#262335")
framemid.grid(row=1, column=1)
framemid1 = Frame(root,background="#262335")
framemid1.grid(row=2, column=1)
framemid2 = Frame(root,background="#262335")
framemid2.grid(row=3, column=1)


#edit password frame
frameright1 = Frame(root,background="#262335")
frameright1.grid(row=1,column=2)

frameright2 = Frame(root,background="#262335")
frameright2.grid(row=2,column=2)

frameright3 = Frame(root,background="#262335")
frameright3.grid(row=3,column=2)

#credit frame
framebottom = Frame(root,background="#262335")
framebottom.grid(row=4,column=0, columnspan=5)


#icon กะว่าจะขอให้เวลาจารย์เช็คโปรแกรมก็ให้โหลดลง download ละชื่อโฟลเดอร์เราคือ password_generator แต่ถ้ายุ่งมากก็ลบไอคอนได้เลย
root.iconbitmap('Downloads\\password_generator\\password.ico')
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.configure(background="#262335")

#line
canvas = Canvas(framemid, width=10, height=155, background='white').pack()
canvas1 = Canvas(framemid1, width=10, height=160, background='white').pack()
canvas2 = Canvas(framemid2, width=10, height=165, background='white').pack()



#heading
Label(frametop, text = 'PASSWORD GENERATOR' , font =('8BIT WONDER',28), fg="#fd62ca", background='#262335').pack(padx=20, pady=20)
Label(frametop, text = '_'*380 , font =('8BIT WONDER',3), fg="#689fe4", background='#689fe4').pack()

#credit
Label(framebottom, text = '_'*380 , font =('8BIT WONDER',3), fg="#689fe4", background='#689fe4').pack(side = BOTTOM)
Label(framebottom, text ='เจนและผองเพื่อน', font ='arial 20 bold', background='#262335', fg='#31ffec').pack(side=BOTTOM)
Label(framebottom, text ='EFGPKPGFE', font =('Mushroom Kingdom NBP Regular',30), fg="#fd62ca", background="#262335").pack(side = BOTTOM)

###select password length

Label(frameleft1, text = 'RANDOM PASSWORD ' , font =('8BIT WONDER',15), fg="#fd62ca", background='#262335').pack(pady=6)
Label(frameleft1, text ='PASSWORD LENGTH', font =('8BIT WONDER',12), fg="#31ffec", background='#262335').pack(padx=10, pady=10)
pass_len = IntVar()
Spinbox(frameleft1, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15, font="arial 15 bold").pack(pady=5)

var_low = IntVar()
var_up = IntVar()
var_spe = IntVar()
var_num = IntVar()

# frameoption.pack(padx=10, pady=10)
Checkbutton(frameoption, text='Upper  ?', variable=var_up, background='#fd62ca', fg="#1914e1").pack(padx=10, pady=5)
Checkbutton(frameoption, text='Lower  ?', variable=var_low, background='#fd62ca', fg="#1914e1").pack(padx=5,pady=5)
Checkbutton(frameoption, text='Special  ?', variable=var_spe, background='#fd62ca', fg="#1914e1").pack(padx=5,pady=5)
Checkbutton(frameoption, text='Number  ?', variable=var_num, background='#fd62ca', fg="#1914e1").pack(padx=5,pady=5)

#####define function
pass_str = StringVar()

def Generator():
    low_letter = [string.ascii_lowercase]
    up_letter = [string.ascii_uppercase]
    special = '$@!%&-_'
    number = [string.digits]
    all_char = low_letter+up_letter+number
    password = []
    if var_num.get() or var_low.get() or var_up.get():
        amount_special = random.choices(list(special), k=pass_len.get()//8*var_spe.get())
        letter = random.choices(all_char, k=pass_len.get()-(pass_len.get()//8*var_spe.get()), weights=[var_low.get(), var_up.get(), var_num.get()])
        for i in letter:
            password += [random.choice(list(i))]
        password = password+amount_special
    elif var_spe.get():
        password = random.choices(list(special), k=pass_len.get())
    else:
        password = ''
    random.shuffle(password)
    password = ''.join(password)
    pass_str.set(password)

###button
Button(frameleft2, text = "GENERATE PASSWORD" , command = Generator, font =('8BIT WONDER',12), fg="#ffffff", background='#689fe4').pack(pady= 10)

Entry(frameleft2 , textvariable = pass_str, fg="red", font =('Nerko One',20)).pack(pady=10)

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(frameleft2, text = 'COPY TO CLIPBOARD', command = Copy_password, font =('8BIT WONDER',12), fg="#ffffff", background='#689fe4').pack(pady=8)

#define function
newpass_str = StringVar()

#Edit weak password to strong password
def Edit():
    password = old_pass.get().replace(' ', '')
    status_low = 0
    status_up = 0
    status_number = 0
    status_special = 0
    last_check = 1
    length = pass_len1.get()
    if password == '':
        status_low, status_number, status_special, status_up, last_check = 1, 1, 1, 1, 0
    if len(password) >= length and (len(password)-length) <= 4:
        locate_del = random.randint(0, len(password)-4)
        if locate_del+4 >= len(password):
            password = password[:locate_del]
        else:
            password = password[:locate_del]+password[locate_del+4:]
    elif len(password) >= length and (len(password)-length) > 4:
        locate_del = random.randint(0, len(password)-(len(password)-length)-4)
        if locate_del+(len(password)-length-4) >= len(password):
            password = password[:locate_del]
        else:
            password = password[:locate_del]+password[locate_del+(len(password)-length)+4:]
    for i in password:
        if i.isupper():
            status_up = 1
        elif i.islower():
            status_low = 1
        elif i.isdigit():
            status_number = 1
        elif i in string.punctuation:
            status_special = 1
    if not all((status_special, status_number, status_low, status_up)):
        if status_number == 0:
            locate = random.randint(0, len(password))
            number = random.randint(0, 9)
            password = password[:locate]+str(number)+password[locate:]
        if status_up == 0 and status_low == 0:
            locate = random.randint(0, len(password))
            lower = random.choice(list(string.ascii_lowercase))
            password = password[:locate]+lower+password[locate:]
            locate = random.randint(0, len(password))
            upper = random.choice(list(string.ascii_uppercase))
            password = password[:locate]+upper+password[locate:]
            status_up = status_low = 1
        elif status_low == 0:
            alpha_list = [i for i in password if i.isupper()]
            random_alpha = random.choice(alpha_list)
            locate = password.find(random_alpha)
            password = password[:locate]+random_alpha.lower()+password[locate+1:]
        elif status_up == 0:
            alpha_list = [i for i in password if i.islower()]
            random_alpha = random.choice(alpha_list)
            locate = password.find(random_alpha)
            password = password[:locate]+random_alpha.upper()+password[locate+1:]
        if status_special == 0 and len(password) >= 8:
            locate = random.randint(0, len(password))
            spe = random.choice(list('$@!&_-'))
            password = password[:locate]+spe+password[locate:]
    if len(password) < length and last_check:
        number = random.choices(list(string.digits), k=abs(len(password)-length)-1)
        password += '_'+''.join(number)
    newpass_str.set(password)

#input old password
Label(frameright1, text = 'EDIT PASSWORD', font =('8BIT WONDER',15), fg="#fd62ca", background='#262335').pack(padx=0, pady=10, side=TOP)
old_pass = StringVar()
Label(frameright1, text ='PASSWORD LENGTH', font =('8BIT WONDER',12), fg="#31ffec", background='#262335').pack(padx=10, pady=10)
pass_len1 = IntVar()
Spinbox(frameright1, from_ = 8, to_ = 32 , textvariable = pass_len1 , width = 15, font="arial 15 bold").pack(pady=5)

#edit password
Entry(frameright2 , fg="red", font =('Nerko One',20), textvariable = old_pass).pack(pady=10)
Button(frameright2, text = "GENERATE PASSWORD" , command = Edit, font =('8BIT WONDER',12), fg="#ffffff", background='#689fe4').pack(pady= 10)
Entry(frameright3 , textvariable = newpass_str, fg="red", font =('Nerko One',20)).pack(pady=10)

#copy new password 
def Copy_newpassword():
    pyperclip.copy(newpass_str.get())
Button(frameright3, text = 'COPY TO CLIPBOARD', command = Copy_newpassword, font =('8BIT WONDER',12), fg="#ffffff", background='#689fe4').pack(pady=8)

# loop to run program
root.mainloop()
