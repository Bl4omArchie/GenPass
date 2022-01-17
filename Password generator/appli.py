#!/usr/bin/python
import string, os, hashlib
from random import randint, choice
from tkinter.messagebox import *
from tkinter import *

def generate_password():
    all_chars = ""
    x = 0
    password_min = s1.get()
    password_max = s2.get()
    maxi = 1000
    
    if password_min == 0:
        password_min = 1
        
    if password_max == 0:
        password_max = password_min
    
    if password_max < password_min:
        x = password_min
        password_min = password_max
        password_max = x

    if int(password_min) > maxi:
        password_min = 1000

    if int(password_max) > maxi:
        password_max = 1000

    if var1.get():
        all_chars = all_chars + string.ascii_lowercase

    if var2.get():
        all_chars = all_chars + string.ascii_uppercase

    if var3.get():
        all_chars = all_chars + string.digits 

    if var4.get():
        all_chars = all_chars + string.punctuation

    if var5.get():
        all_chars = string.ascii_letters + string.punctuation + string.digits
        
    if all_chars != "":
        print (password_max)
        password = "".join(choice(all_chars) for x in range(randint(int(password_min), int(password_max))))
        password_entry["state"] = "normal"
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        password_entry["state"] = "disabled"

        with open("log.txt", "a") as fp:
            fp.write(password)
            fp.write("\n")

def open_file():
    os.system("log.txt")

def clear_file():
    if askyesno("Clear file", "Do you really want to clear the file ?"):
        showinfo("Cleared", "The file is now clear !")
        os.remove("log.txt")
    else:
        showinfo("Unclear", "Not clear")

def about():
    window2 = Tk()
    window2.title("About")
    window2.geometry("1100x800")
    window2.iconbitmap("info.ico")
    window.config(background='#2f3136')

    #about the tool
    l = LabelFrame(window2, text="About the tool", bg='#40444D', font=("Courier New", 15), padx=30, pady=30)
    l.pack(fill="both", expand="yes")
    
    about_label = Label(l, text="This tool generate strong passwords for the security of your accounts. \nYou can easily generate passwords and manage them with a file wich saves all the generated passwords", font=("Arial Black", 10), bg='#40444D').pack()
    about_label2 = Label(l, text="The maximum generation issues of this tool is 96**1000 (it's a lot)", font=("Arial Black", 10), bg='#40444D').pack()
    about_label2 = Label(l, text="This tool was created by 4 cats, 1 dog and Elon Musk himself", font=("Arial Black", 10), bg='#40444D').pack()
    
    #how the tool working
    l2 = LabelFrame(window2, text="How the tool working", bg='#40444D', font=("Courier New", 15), padx=30, pady=30)
    l2.pack(fill="both", expand="yes")
    
    work_label = Label(l2, text="The characters generated range from 1 to 1000 (if you put more than 1000, the program will automatically remove the max value to 1000).\n You can regulate the minimum and maximum\n", font=("Arial Black", 10), bg='#40444D').pack()
    work_label2 = Label(l2, text="If you put a minimum value bigger than the maximum value, the values will be switch.\n", font=("Arial Black", 10), bg='#40444D').pack()
    work_label3 = Label(l2, text="You can chose into lowercases, uppercases, poncuation, numbers or everything in the same time\nIf you select anything, the tool will generate nothing\n", font=("Arial Black", 10), bg='#40444D').pack()
    work_label4 = Label(l2, text="All the passwords you generate will be saved in a file named log.txt. Please: don't touch this file for the good operating of the tool", font=("Arial Black", 10), bg='#40444D').pack()
    work_label5 = Label(l2, text="With the toolbar you can open this file, see all your generated passwords and also clear the file\nIf you clear the file, you can't open up a new one, you first nead to generate a new password\n", font=("Arial Black", 10), bg='#40444D').pack()
    work_label3 = Label(l2, text="When you finally chose the options you want, you can click on the button generate and you password will be created !\n", font=("Arial Black", 10), bg='#40444D').pack()

    #creator
    l3 = LabelFrame(window2, text="Creator", bg='#40444D', font=("Courier New", 15), padx=30, pady=30)
    l3.pack(fill="both", expand="yes")
    
    creator_label = Label(l3, text="Created by Archie Bloom#1337\nGUI: Tkinter\nWith the help of friends\nThis tool is open source, you can use the code for yourself", font=("Arial Black", 10), bg='#40444D').pack()
        
    frame.pack(expand=YES)
    window.mainloop()

window = Tk()
window.title("Password Generator")
window.geometry("1250x750")

window.iconbitmap("password.ico")
window.config(background='#2f3136')

var1, var2, var3, var4, var5 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
password_min, password_max = 0, 0

frame = Frame(window, bg='#2f3136')
frame2 = Frame(window, bg='#40444D')

right_frame = Frame(frame, bg='#2f3136')
under_frame = Frame(frame2, bg='#40444D')

#title
label_title = Label(right_frame, text="Password", font=("Courier New", 40), bg='#2f3136', fg='white')
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 30), disabledforeground='white', width=50, state="disabled", disabledbackground="#40444D")
password_entry.pack()

# checkbutton
bouton = Checkbutton(under_frame, text="lowercases characters", font=("Courier New", 12), bg='#40444D', variable=var1)
bouton.deselect()
bouton.pack(side=LEFT, padx=10, pady=10)

bouton2 = Checkbutton(under_frame, text="uppercases characters", font=("Courier New", 12), bg='#40444D', variable=var2)
bouton2.deselect()
bouton2.pack(side=LEFT, padx=10, pady=10)

bouton3 = Checkbutton(under_frame, text="numbers", bg='#40444D', font=("Courier New", 12), variable=var3)
bouton3.deselect()
bouton3.pack(side=LEFT, padx=10, pady=10)

bouton4 = Checkbutton(under_frame, text="ponctuation", bg='#40444D', font=("Courier New", 12), variable=var4)
bouton4.deselect()
bouton4.pack(side=LEFT, padx=10, pady=10)

bouton5 = Checkbutton(under_frame, text="everything", bg='#40444D', font=("Courier New", 12), variable=var5)
bouton5.deselect()
bouton5.pack(side=LEFT, padx=10, pady=10)

#generation boutton
generate_password_button = Button(right_frame, text="Generate password", font=("Courier New", 30), bg='#40444D', fg='white',command=generate_password)
generate_password_button.pack(fill=X)

#label
min_label = Label(right_frame, text="Min:", font=("Courier New", 20), bg='#40444D', fg='white')
min_label.pack(side=LEFT, padx=5, pady=5)

#spinbox
s1 = Spinbox(right_frame, from_=1, to=150)
s1.pack(side=LEFT,padx=3, pady=3)

#label
max_label = Label(right_frame, text="Max:", font=("Courier New", 20), bg='#40444D', fg='white')
max_label.pack(side=LEFT, padx=5, pady=5)

s2 = Spinbox(right_frame, from_=1, to=1000)
s2.pack(side=LEFT,padx=3, pady=3)

right_frame.grid(row=0, column=1, sticky=W)
under_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)
frame2.pack(expand=YES)

#menu declarations
menu_bar = Menu(window)
menu1 = Menu(menu_bar, tearoff=0)
menu2 = Menu(menu_bar, tearoff=0)

menu1.add_command(label="Open", command=open_file)
menu1.add_command(label="Clear", command=clear_file)
menu1.add_separator()
menu1.add_command(label="Quit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=menu1)

menu2.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=menu2)

window.config(menu=menu_bar)
window.mainloop()
