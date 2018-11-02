import Tkinter as tk
from Tkinter import *
import sqlite3

import tkMessageBox
from Tkinter import *
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
conn.commit()
def ff(a):
	a.pack()	
	a.tkraise()
def back():
	f.pack_forget()
	#f.lower()
	can.pack(fill = BOTH)
	can.tkraise()
def home(a):
	a.pack_forget()
	can.pack()
	can.tkraise()	
def bag(a):
	a.pack()
	g.pack_forget()
	a.tkraise()	
def bagback():
	i.pack_forget()
	g.pack()
	g.tkraise()
def genget():
	gend = sel.get()
	return gend	
def bgget():
	value = bgp.get()
	return value	
def sub():
# associated with frame f
	val1 = did.get()
	val2 = named.get()
	val3 = adden.get()
	val4 = bgget()
	val5 = disen.get()
	val6 = hem.get()
	val7 = age.get()
	val8 = wet.get()
	val9 = genget()
	val10 = mobile.get()
	sql1 = "INSERT INTO donor values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
	c.execute(sql1, (val1, val2, val3, val4, val5, val6, val7, val8, val9, val10))
	conn.commit()
	tkMessageBox.showinfo('Success!','Successfully added to database')
	did.delete(0, END)
	named.delete(0, END)
	adden.delete(0, END)
	disen.delete(0, END)
	hem.delete(0, END)
	age.delete(0, END)
	wet.delete(0, END)
	mobile.delete(0, END)
	
def sup():
# frame H
	v1 = namen.get()
	v2 = cnon.get()
	v3 = dobn.get()
	v4 = addrn.get()
	v5 = cityn.get()
	v6 = pinn.get()
	v7 = empidn.get()
	v8 = postn.get()
	v9 = pwdn.get()
	sql2 = "INSERT INTO employee values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
	c.execute(sql2, (v1, v2, v3, v4, v5, v6, v7, v8, v9))
	conn.commit()
	tkMessageBox.showinfo('Saved!','Successfully signed up')
	namen.delete(0, END)
	cnon.delete(0, END)
	dobn.delete(0, END)
	addrn.delete(0, END)
	cityn.delete(0, END)
	pinn.delete(0, END)
	empidn.delete(0, END)
	postn.delete(0, END)
	pwdn.delete(0, END)

def savethis():
# frame i
	va1 = bcode1n.get()
	va2 = btype1n.get()
	va3 = cost1n.get()
	va4 = coldate1n.get()
	va5 = expdate1n.get()
	sql3 = "INSERT INTO blood_store VALUES(?, ?, ?, ?, ?)"
	c.execute(sql3, (va1, va2, va3, va4, va5))
	conn.commit()
	tkMessageBox.showinfo('Saved!','Successfully saved blood bag')
	bcode1n.delete(0, END)
	btype1n.delete(0, END)
	cost1n.delete(0, END)
	coldate1n.delete(0, END)
	expdate1n.delete(0, END)
def expofun():
# frame k
	n1 = trans_id2.get()
	n2 = date2.get()
	n3 = 'SENT'
	n4 = qty2.get()
	n5 = bank2.get()
	sq4 = "INSERT INTO transac values (?, ?, ?, ? , ?)" 
	c.execute(sq4, (n1, n2, n3 , n4 , n5))	
	conn.commit()
	tkMessageBox.showinfo('Exported!','Successfully exported blood')
	trans_id2.delete(0, END)
	date2.delete(0, END)
	qty2.delete(0, END)
	bank2.delete(0, END)
def expback():
	k.pack_forget()			
	j.pack()
	j.tkraise()
def expbtn():
	j.pack_forget()
	k.pack()
	k.tkraise()	
def impbtn():
	j.pack_forget()
	z.pack()
	z.tkraise()
def impback():
	z.pack_forget()
	j.pack()
	j.tkraise()
def impofun():	
# frame z
	m1 = trans_id2z.get()
	m2 = date2z.get()
	m3 = 'RECIEVED'
	m4 = qty2z.get()
	m5 = bank2z.get()
	sq4 = "INSERT INTO transac values (?, ?, ?, ?, ?)" 
	c.execute(sq4, (m1, m2, m3 , m4 , m5))	
	conn.commit()
	tkMessageBox.showinfo('imported!','Successfully imported blood')
	trans_id2z.delete(0, END)
	date2z.delete(0, END)
	qty2z.delete(0, END)
	bank2z.delete(0, END)	
		
		
vm = Tk()
vm.title("Blood Bonds")
can = Frame(vm, width = 1000, height = 700)
can.configure(background = 'white')
title = Label(can, text = 'Blood Bank system', font = ('verdana 20'))

#Frame ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff 

f = Frame(can, width = 1000, height = 700)
f.configure(background = 'white')
lb = Label(f, text = 'New Donor Registration', font = ('verdana 14'))

bbtn = Button(f, text = 'Back', command = lambda: back())
bbtn.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
bbtn.place(relx = 0.02, rely = 0.02)

named = Entry(f, width = 50)
nm = Label(f, text = 'Name: ')
nm.place(relx = 0.05, rely = 0.15)
named.place(relx = 0.11, rely = 0.15)
lb.place(relx = 0.1, rely = 0.1)


age = Entry(f, width = 10)
nage = Label(f, text = 'Age: ')
nage.place(relx = 0.05, rely = 0.2)
age.place(relx = 0.1, rely = 0.2)

sel = StringVar()
sel.set('Male')
gen = Label(f, text = 'Gender')
gender = OptionMenu(f, sel,'Male', 'Female', 'Other')
gender.place(relx = 0.32, rely = 0.19)
gen.place(relx = 0.26, rely = 0.2)

wet = Entry(f, width = 10)
wname = Label(f, text = 'weight: ')
wet.place(relx = 0.12, rely = 0.25)
wname.place(relx = 0.05, rely = 0.25)

hem = Entry(f, width = 10)
hemnm = Label(f, text = 'Haemoglobin: ')
hemnm.place(relx = 0.05, rely = 0.3)
hem.place(relx = 0.16, rely = 0.3)

bgp = StringVar()
bgp.set('O +ve')
bgrp = OptionMenu(f, bgp, 'O +ve', 'O -ve', 'A +ve', 'A -ve', 'B +ve', 'B -ve', 'AB +ve', 'AB -ve')
bgname = Label(f, text = 'Blood Group: ')
bgrp.place(relx = 0.38, rely = 0.29)
bgname.place(relx = 0.28, rely = 0.3)

addr = Label(f, text = 'Address:')
adden = Entry(f, width = 50)
addr.place(relx = 0.05, rely = 0.36)
adden.place(relx = 0.12, rely = 0.36)

med = Checkbutton(f)
medx = Label(f, text = 'Not taken medicine in last 24 hours')
medx.place(relx = 0.05, rely = 0.41)
med.place(relx = 0.3, rely = 0.41)

dis = Label(f, text = 'Disease (if any) :')
dis.place(relx = 0.05, rely = 0.46)
disen = Entry(f, width = '25')
disen.place(relx = 0.18, rely = 0.46)

mob = Label(f, text = 'Mobile no: ')
mob.place(relx = 0.05, rely = 0.51)
mobile = Entry(f, width = 20)
mobile.place(relx = 0.14, rely = 0.51)

did = Entry(f, width = 20)
did.place(relx = 0.1, rely = 0.56)
d_id = Label(f, text = 'ID: ')
d_id.place(relx = 0.05, rely = 0.56)

submit = Button(f, text = 'Submit', command = lambda: sub())
submit.config(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
submit.place(relx = 0.3, rely = 0.8)
#Frame ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff	
# FRAME GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
g = Frame(can, width = 1000, height = 700)
g.configure(background = 'white')
stor = Label(g, text = 'Total bags: ')

amt = IntVar()	
sq3 = "SELECT COUNT(barcode) FROM blood_store"
c.execute(sq3)
amt = 0
amt = c.fetchall()
amt = amt[0]
conn.commit()
stamt = Label(g, text = amt, bg = 'white')	
adbtn = Button(g, text = 'Add blood bag', command = lambda: bag(i))
adbtn.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
backbtn = Button(g, text = 'Back', command = lambda: home(g))
backbtn.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
bcode = Label(g, text = 'BarCode')
btype = Label(g, text = 'Type ')
cost =  Label(g, text = 'Cost')
coldate = Label(g, text = 'Collection date', bg = 'white')
expdate = Label(g, text = 'Expiry date')
sq = "SELECT * FROM  blood_store"
c.execute(sq)
px = c.fetchall()
conn.commit()
l = 0.2
# printing loop
for x in px:		
	t1,t2,t3,t4,t5 = x
	t = str(t1) + '    ' + t2 + '\t  ' + str(t3) + '\t' + t4 + '\t' + t5
	data = Label(g, text = t)
	data.place(relx = 0.18, rely = l)
	l += 0.05
expdate.place(relx = 0.45, rely = 0.15) 
stor.place(relx = 0.08, rely = 0.1)
stamt.place(relx = 0.18, rely = 0.1)
adbtn.place(relx = 0.85, rely = 0.1)
cost.place(relx = 0.32, rely = 0.15)
backbtn.place(relx = 0.02, rely = 0.02)
bcode.place(relx = 0.18, rely = 0.15)
btype.place(relx = 0.26, rely = 0.15)
coldate.place(relx = 0.35, rely = 0.15) 

# Frame GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG	
# FRAME HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHhhHHHHHHH
#sign up page
h = Frame(can, width = 1000, height = 700)
h.configure(background = 'white')
Sign = Label(h, text = 'Sign Up !', font = ('verdana 14'))
name = Label(h, text = 'Name')
namen = Entry(h, width = 50)
cno = Label(h, text = 'contact no: ')
cnon = Entry(h, width = 17)
dob = Label(h, text = 'DOB :')
dobn = Entry(h, width = 17)
addr = Label(h, text = 'Address :')
addrn = Entry(h, width = 50)
city  = Label(h, text = 'City :')
cityn = Entry(h, width = 20)
pin = Label(h , text = 'Pin Code : ')
pinn = Entry(h, width = 12)
empid = Label(h, text = 'Employee ID :')
empidn = Entry(h, width = 20)
pwd = Label(h, text = 'Password :')
pwdn = Entry(h, width = 20)
tmc = Label(h, text = 'I agree the Terms and Conditions')
tmcb = Checkbutton(h)
post = Label(h, text = 'Designation :')
postn = Entry(h, width = 25)

bckbtn = Button(h, text = 'Back', command = lambda: home(h))
bckbtn.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
bckbtn.place(relx = 0.02, rely = 0.02)
SU = Button(h, text = ' Sign Up ', command = lambda: sup())
SU.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
#places:
Sign.place(relx = 0.3, rely = 0.05)
name.place(relx = 0.05, rely = 0.1)
namen.place(relx = 0.1, rely = 0.1)
cno.place(relx = 0.05, rely = 0.15)
cnon.place(relx = 0.15, rely = 0.15)
dob.place(relx = 0.3, rely = 0.15)
dobn.place(relx = 0.35, rely = 0.15)
addr.place(relx = 0.05, rely = 0.20)
addrn.place(relx = 0.13, rely = 0.20)
city.place(relx = 0.05, rely = 0.25)
cityn.place(relx = 0.12, rely = 0.25)
pin.place(relx = 0.34, rely = 0.25)
pinn.place(relx = 0.42, rely = 0.25)
empid.place(relx = 0.05, rely = 0.3)
empidn.place(relx = 0.16, rely = 0.3)
post.place(relx = 0.35, rely = 0.3)
postn.place(relx = 0.45, rely = 0.3)
pwd.place(relx = 0.05, rely = 0.35)
pwdn.place(relx = 0.14, rely = 0.35)
tmc.place(relx = 0.33, rely = 0.45	)
tmcb.place(relx = 0.3, rely = 0.45)
SU.place(relx = 0.3, rely = 0.52)

# FRAME HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# FRAME IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
i = Frame(can, width = 1000, height = 700)
i.configure(background = 'white')
addbag = Label(i, text = ' ADD BLOOD-BAG INFO ')

bcode1 = Label(i, text = 'BarCode :')
bcode1n = Entry(i, width = 15)
btype1 = Label(i, text = 'Type :')
btype1n = Entry(i, width = 15)
cost1 =  Label(i, text = 'Cost :')
cost1n =  Entry(i, width = 15)
coldate1 = Label(i, text = 'Collection date :')
coldate1n = Entry(i, width = 15)
expdate1 = Label(i, text = 'Expiry date :')
expdate1n = Entry(i, width = 15)
save = Button(i, text = 'SAVE and EXIT', command = lambda: savethis())
save.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')

cancel = Button(i, text = 'Cancel', command = lambda: bagback())
cancel.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
cancel.place(relx = 0.02, rely = 0.02)
# PLACEMENT
bcode1.place(relx = 0.1, rely = 0.1)
bcode1n.place(relx = 0.18, rely = 0.1)
btype1.place(relx = 0.1, rely = 0.15)
btype1n.place(relx = 0.18, rely = 0.15)
cost1.place(relx = 0.1, rely = 0.2)
cost1n.place(relx = 0.18, rely = 0.2)
coldate1.place(relx = 0.1, rely = 0.25)
coldate1n.place(relx = 0.22, rely = 0.25)
expdate1.place(relx = 0.1, rely = 0.3)
expdate1n.place(relx = 0.22, rely = 0.3)
save.place(relx = 0.2, rely = 0.35)
addbag.place(relx = 0.12, rely = 0.05)
# FRAME IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
# FRAME JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
j = Frame(can, width = 1000, height = 700)
j.configure(background = 'white')
trans = Label(j, text = ' Transactions ', font = ('verdana 14'))
exp = Button(j, text = 'export blood', command = lambda: expbtn())
imp = Button(j, text = 'Import blood', command = lambda: impbtn())

exp.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
imp.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
bakbtn = Button(j, text = 'Back', command = lambda: home(j))
bakbtn.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
datte = Label(j, text = 'DATE')
sent = Label(j, text = 'SENT/RECIEVED')

qty = Label(j, text = 'QUANTITY')
bankco = Label(j, text = 'BLOOD_BANK_CODE')
trans_id = Label(j, text = 'trans_id')
sq2 = "SELECT * FROM transac"
c.execute(sq2)
pk = c.fetchall()
conn.commit()
u = 0.25
# LOOPING FUNCTION label
for o in pk:		
	k1,k2,k3,k4,k5 = o
	tm = str(k1) + '\t' + str(k2) + '\t ' + str(k3) + '\t' + str(k4) + '\t' + str(k5)
	tmp = Label(j, text = tm)
	tmp.place(relx = 0.05, rely = u)
	u += 0.05

trans_id.place(relx = 0.05, rely =0.2)
datte.place(relx = 0.15, rely = 0.2)
sent.place(relx = 0.21, rely = 0.2)
qty.place(relx = 0.34, rely = 0.2)
bankco.place(relx = 0.42, rely = 0.2)
bakbtn.place(relx = 0.02, rely = 0.02)
exp.place(relx = 0.7, rely = 0.05)
imp.place(relx = 0.85, rely = 0.05)
#trans.place(relx = 0.15, rely = 0.05)      #what is this?
# fRAME JJJJJJJJJJJJJJjjjjjjjjjjjjjjjjJJJJJJJJJJJJJJJJJJJJJJJJJJjjjjjjjjjjjjjjjjjjJJJJJJJJJJJJJJJJJ
# FRAMEE kkkkkkkkkkkkkkkkkkkkkkkkkkkkKKKKKKKKKKKKKKKKkkkkkkkkkkkkKKKKKKKKKKKKKKKKkkkkkkkkkkkKKKKKK
k = Frame(can, width = 1000, height = 700)
k.configure(background = 'white')
trans_id1 = Label(k, text = 'Transactoin ID')
trans_id2 = Entry(k, width = 20)
date1 = Label(k, text = 'Date: ')
date2 = Entry(k, width = 20)
qty1 = Label(k, text = 'Quantity :')
qty2 = Entry(k, width = 20)
bank1 = Label(k, text = 'Blood Bank ID: ')
bank2 = Entry(k , width = 20)
exp1 = Button(k, text = 'Export', command = lambda: expofun())
exp1.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
cancel1 = Button(k, text = 'Cancel', command = lambda: expback())
cancel1.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
says = Label(k, text = 'Export blood to other blood banks', font = ('verdana 15'))

cancel1.place(relx = 0.02, rely = 0.02)
date1.place(relx = 0.1, rely = 0.14)
date2.place(relx = 0.15, rely = 0.14)
qty1.place(relx = 0.1, rely = 0.2)
qty2.place(relx = 0.18, rely = 0.2)
bank1.place(relx = 0.1, rely = 0.25)
bank2.place(relx = 0.215, rely = 0.25)
exp1.place(relx = 0.26, rely = 0.40)
trans_id1.place(relx = 0.1, rely = 0.30)
trans_id2.place(relx = 0.215, rely = 0.30)
says.place(relx = 0.15, rely = 0.08)
# FRAMEE kkkkkkkkkkkkkkkkkkkkkkkkkkkkKKKKKKKKKKKKKKKKkkkkkkkkkkkkKKKKKKKKKKKKKKKKkkkkkkkkkkkKKKKKK
# FRAME ZzzzzzzzzzzZZZZZZZZZZZZZZZZZzzzzzzzzzzzZZZZZZZZZZZZZZZZZZZZZZZZZZZZzzzzzzzzzzzzzzzZZZZZZZZZZ
z = Frame(can, width = 1000, height = 700)
z.configure(background = 'white')

say = Label(z, text = 'Import blood from other blood banks', font = ('verdana 15'))
trans_id1z = Label(z, text = 'Transactoin ID')
trans_id2z = Entry(z, width = 20)
date1z = Label(z, text = 'Date: ')
date2z = Entry(z, width = 20)
qty1z = Label(z, text = 'Quantity :')
qty2z = Entry(z, width = 20)
bank1z = Label(z, text = 'Blood Bank ID: ')
bank2z = Entry(z, width = 20)
exp1z = Button(z, text = 'Import', command = lambda: impofun())
exp1z.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
cancel1z = Button(z, text = 'Cancel', command = lambda: impback())
cancel1z.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')

cancel1z.place(relx = 0.02, rely = 0.02)
date1z.place(relx = 0.1, rely = 0.14)
date2z.place(relx = 0.15, rely = 0.14)
qty1z.place(relx = 0.1, rely = 0.2)
qty2z.place(relx = 0.18, rely = 0.2)
bank1z.place(relx = 0.1, rely = 0.25)
bank2z.place(relx = 0.215, rely = 0.25)
exp1z.place(relx = 0.26, rely = 0.40)
trans_id1z.place(relx = 0.1, rely = 0.30)
trans_id2z.place(relx = 0.215, rely = 0.30)
say.place(relx = 0.15, rely = 0.08)
# FRAME ZzzzzzzzzzzZZZZZZZZZZZZZZZZZzzzzzzzzzzzZZZZZZZZZZZZZZZZZZZZZZZZZZZZzzzzzzzzzzzzzzzZZZZZZZZZZ
btn1 = Button(can, text = 'New donor', command = lambda: ff(f))
btn1.place(relx = 0.1, rely = 0.18)
btn1.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
btn2 = Button(can, text = 'Blood inventory', command = lambda: ff(g))
btn2.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
btn2.place(relx = 0.3, rely = 0.18)

btn3 = Button(can, text = 'Transactions',command = lambda: ff(j))
btn3.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
btn3.place(relx = 0.52, rely = 0.18)

btn4 = Button(can, text = 'Sign Up!', command = lambda: ff(h))
btn4.configure(bg= '#4d4d4d', bd = '0', activebackground = '#737373', fg = 'white')
btn4.place(relx = 0.85, rely = 0.05)

can.pack()
title.place(relx = 0.02, rely = 0.03)
vm.mainloop()
