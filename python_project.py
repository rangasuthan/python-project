import mysql.connector as sqltor
from tkinter import *
from tkinter import messagebox
import tempfile
import os

mycon = sqltor.connect(host='localhost', user='root', password='dbase2005', database='dusky')
if mycon.is_connected():
    print('connected..')
cursor = mycon.cursor()


def pet():
    n = int(input('enter the  how many type of pets u want :'))
    for i in range(n):
        x = input('what pet u want to purchase:')
        if x in s:
            a = s[x]
        else:
            print('pet is not in shop')
        y = int(input('enter the quantities:'))
        if a > y:
            a = a - y
            print('current', x, 'in current stok is:', a)
            print('sno=1 is dog,sno=2 is cat,sno=3 is fish')
            gomma = int(input('enter the sno to update the pet table:'))
            gomma1 = s[x] - y
            st = 'update pet set quantity={} where sno={}'.format(gomma1, gomma)
            cursor.execute(st)
            mycon.commit()
            print(y, x, 'purshased')
        else:
            print(x, 'is out of stock')

    print('pet purchased successfully')
    print('***')
    ans = input('do u want buy pet_food for ur pet (y/n):')
    if ans == 'y':
        pet_food()
    else:
        print('thank u')


def pet_food():
    n1 = int(input('enter how many pet_food_varitey u need:'))
    for k in range(n1):
        print('types of food are=', pf)
        el = input('enter petfood u need:')
        quantity_petfood = int(input('enter the quantity:'))
        print('sno=1 pedigree,sno=2 tuna,sno=3 floating pelletes,sno=4 white kangni seeds')
        pff = int(input('enter sno of pet food u need:'))
        pf1 = pf[el] - quantity_petfood
        if pf[el] > quantity_petfood:
            print(el, pf1, 'is the current pet food quantity')
            st1 = 'update petfood set quantity={} where sno={}'.format(pf1, pff)
            cursor.execute(st1)
            mycon.commit()
            print('pet food purchased sucessfully')
            print('thank u')

        st1 = 'update petfood set quantity={} where sno={}'.format(pf1, pff)
        cursor.execute(st1)
        mycon.commit()
        print('pet food purchased sucessfully')
        print('thank u')


print('***')
print('welcome to dusky pet shop')
print('buy our healthy and joful pets')
print('choice-1 is pets for sale,choice-2 is for pet food')
choice = int(input('enter ur choice:'))
s = {'dog': 130, 'cat': 200, 'fish': 300}
indianbreed = {'rajapalayam': 26, 'kombai': 52, 'gulldong': 30}
foriegnbreed = {'germanshepherd': 6, 'boxer': 3, 'pug': 13}
pf = {'pedigree': 300, 'tuna': 380, 'floating pelletes': 400, 'white kangni seeds': 350}
if choice == 1:
    pet()

elif choice == 2:
    pet_food()

root = Tk()
root.title('Pet billing system')
root.geometry('1280x720')
bg_color = '#2D9290'

# -------------identifiers-----------
Dog = IntVar()
Cat = IntVar()
Fish = IntVar()
Petfood = IntVar()
total = IntVar()

cb = StringVar()
cw = StringVar()
cr = StringVar()
cm = StringVar()
total_cost = StringVar()


# -----------functions----------------
def Total():
    if Dog.get() == 0 and Cat.get() == 0 and Fish.get() == 0 and Petfood.get() == 0:
        messagebox.showerror('Error', 'Please select number of quantity')
    else:
        b = Dog.get()
        w = Cat.get()
        r = Fish.get()
        m = Petfood.get()

        t = float(b * 1000.89 + w * 8000.99 + r * 250.18 + m * 400.50)
        total.set(b + w + r + m)
        total_cost.set('$' + str(round(t, 2)))
        cb.set('$' + str(round(b * 1000.89, 2)))
        cw.set('$' + str(round(w * 8000.99, 2)))
        cr.set('$' + str(round(r * 250.18, 2)))
        cm.set('$' + str(round(m * 400.50, 2)))


def receipt():
    textarea.delete(1.0, END)
    textarea.insert(END, 'Pets\tNumber of Items\tCost of items')
    textarea.insert(END, f"\n\nDog\t\t{Dog.get()}\t {cb.get()}")
    textarea.insert(END, f"\n\nCat\t\t{Cat.get()}\t {cw.get()}")
    textarea.insert(END, f"\n\nFish\t\t{Fish.get()}\t {cr.get()}")
    textarea.insert(END, f"\n\nPetfood\t\t{Petfood.get()}\t {cm.get()}")
    textarea.insert(END, '\n\n================================')
    textarea.insert(END, f"\n\ntotal\t\t{total.get()}\t {total_cost.get()}")
    textarea.insert(END, '\n\n================================')


def print():
    q = textarea.get('1.0', 'end-1c')
    filename = tempfile.mktemp('.txt')
    open(filename, 'w').write(q)
    os.startfile(filename, 'Print')


def reset():
    textarea.delete(1.0, END)
    Dog.set(0)
    Cat.set(0)
    Fish.set(0)
    Petfood.set(0)
    total.set(0)

    cb.set('')
    cw.set('')
    cr.set('')
    cm.set('')
    total_cost.set('')


def exit():
    if messagebox.askyesno('Exit', 'Do you really want to exist'):
        root.destroy()


title = Label(root, text='Pet billing system', bg=bg_color, fg='white', font=('times new romman', 35, 'bold'),
              relief=GROOVE, bd=12)
title.pack(fill=X)

# -------------product details------------
F1 = LabelFrame(root, text='Product Details', font=('times new romman', 20, 'bold'), fg='gold', bg=bg_color,
                relief=RIDGE, bd=16)
F1.place(x=5, y=98, width=800, height=500)

# -------heading-----------
itm = Label(F1, text='Pets', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
itm.grid(row=0, column=0, padx=20, pady=15)
n = Label(F1, text='Items', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
n.grid(row=0, column=1, padx=20, pady=15)
cost = Label(F1, text='Cost', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
cost.grid(row=0, column=2, padx=20, pady=15)

# --------pets--------------
dog = Label(F1, text='Dog', font=('times new romman', 20, 'bold'), fg='lawngreen', bg=bg_color)
dog.grid(row=1, column=0, padx=20, pady=15)
b_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=Dog)
b_txt.grid(row=1, column=1, padx=20, pady=15)
cb_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cb)
cb_txt.grid(row=1, column=2, padx=20, pady=15)

cat = Label(F1, text='Cat', font=('times new romman', 20, 'bold'), fg='lawngreen', bg=bg_color)
cat.grid(row=2, column=0, padx=20, pady=15)
c_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=Cat)
c_txt.grid(row=2, column=1, padx=20, pady=15)
cc_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cw)
cc_txt.grid(row=2, column=2, padx=20, pady=15)

fish = Label(F1, text='Fish', font=('times new romman', 20, 'bold'), fg='lawngreen', bg=bg_color)
fish.grid(row=3, column=0, padx=20, pady=15)
f_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=Fish)
f_txt.grid(row=3, column=1, padx=20, pady=15)
cd_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cr)
cd_txt.grid(row=3, column=2, padx=20, pady=15)

prod = Label(F1, text='Pet Food', font=('times new romman', 20, 'bold'), fg='lawngreen', bg=bg_color)
prod.grid(row=4, column=0, padx=20, pady=15)
p_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=Petfood)
p_txt.grid(row=4, column=1, padx=20, pady=15)
cp_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cm)
cp_txt.grid(row=4, column=2, padx=20, pady=15)

t = Label(F1, text='Total Price', font=('times new romman', 20, 'bold'), fg='lawngreen', bg=bg_color)
t.grid(row=5, column=0, padx=20, pady=15)
t_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=total)
t_txt.grid(row=5, column=1, padx=20, pady=15)
ct_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=total_cost)
ct_txt.grid(row=5, column=2, padx=20, pady=15)

# -----------bill area-------------------
F2 = Frame(root, relief=GROOVE, bd=10)
F2.place(x=820, y=90, width=430, height=500)
bill_title = Label(F2, text='Receipt', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
scrol = Scrollbar(F2, orient=VERTICAL)
scrol.pack(side=RIGHT, fill=Y)
textarea = Text(F2, font='arial 15 bold', yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

# -----------button-------------
F3 = Frame(root, relief=GROOVE, bd=10, bg=bg_color)
F3.place(x=5, y=590, width=1270, height=120)

btn1 = Button(F3, text='Total', font='arial 25 bold', bg='yellow', fg='red', width=10, padx=5, pady=5, command=Total)
btn1.grid(row=0, column=0, padx=20, pady=10)

btn2 = Button(F3, text='Receipt', font='arial 25 bold', bg='yellow', fg='red', width=10, padx=5, pady=5,
              command=receipt)
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = Button(F3, text='Print', font='arial 25 bold', bg='yellow', fg='red', width=10, padx=5, pady=5, command=print())
btn3.grid(row=0, column=2, padx=10, pady=10)

btn4 = Button(F3, text='Reset', font='arial 25 bold', bg='yellow', fg='red', width=10, padx=5, pady=5, command=reset())
btn4.grid(row=0, column=3, padx=10, pady=10)

btn5 = Button(F3, text='Exit', font='arial 25 bold', bg='yellow', fg='red', width=10, padx=5, pady=5, command=exit)
btn5.grid(row=0, column=4, padx=10, pady=10)
root.mainloop()

"""MYSQL CODE:
Create database dusky
Use dusky
Create table pet(sno int,petname varchar(20),quantity int)
Create table petfood(sno int,pet_food varchar(20),quantity 
int"""
