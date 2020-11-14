# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:13:29 2020

@author: Luis Navarro
"""

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x600")

window.title("SPE Assignment 1")

# =============================================================================
# Capillary problem
# =============================================================================
def rc(t2,theta,t1,t3):
    rc = (2*int_tension*np.cos(theta))/(cP)
    return (rc)
    messagebox.showinfo("Title", "Tube radious =",rc)

#Header
l1 = Label(window,text = "Capilarity problem")
l1.grid(row = 0,column = 1)
#1st row
l2 = Label(window,text = "Theta value =")
l2.grid(row = 1,column =0 )
theta = StringVar()
t1 = Entry(window, textvariable = theta)
t1.grid (row=1,column=1)
#2nd row
l3 = Label(window,text = "Interfacial Tension =")
l3.grid(row = 2,column =0)
int_tension = StringVar()
t2 = Entry(window, textvariable = int_tension)
t2.grid (row=2,column=1)
#3rd row
l3 = Label(window,text = "Capillary pressure =")
l3.grid(row = 3,column =0 )
cP = StringVar()
t3 = Entry(window, textvariable = cP)
t3.grid (row=3,column=1)
#Button
b1 = Button(window, text = "Tube Radius", command = rc)
b1.grid (row=3,column=3)

# =============================================================================
# Permeability value
# =============================================================================
def k(q,mu,Bo,m,h):
    k = (162.6*q*mu*Bo)/(m*h)
    return (k)
#Header
l4 = Label(window,text = "Permeability problem")
l4.grid(row = 4,column = 1)
#1st row
l5 = Label(window,text = "Rate =")
l5.grid(row = 5,column =0 )
q = StringVar()
t4 = Entry(window, textvariable = q)
t4.grid (row=5,column=1)
#2nd row
l6 = Label(window,text = "Viscosity =")
l6.grid(row = 6,column =0)
mu = StringVar()
t5 = Entry(window, textvariable = mu)
t5.grid (row=6,column=1)
#3rd row
l7 = Label(window,text = "Production time =")
l7.grid(row = 7,column =0 )
m = StringVar()
t5 = Entry(window, textvariable = m)
t5.grid (row=7,column=1)
#4th row
l6 = Label(window,text = "Formation Heigth =")
l6.grid(row = 8,column =0)
mu = StringVar()
t5 = Entry(window, textvariable = mu)
t5.grid (row=8,column=1)
#5th row
l7 = Label(window,text = "Oil Volume Factor =")
l7.grid(row = 9,column =0)
Bo = StringVar()
t6 = Entry(window, textvariable = Bo)
t6.grid (row=9,column=1)
#Button
b2 = Button(window, text = "Permeability", command = k)
b2.grid (row=9,column=3)
# =============================================================================
# Skin Factor
# =============================================================================
def s(p_1hr,p_wf,phi,mu,rw):
    ct = 22.6*10**(-6)
    s = (1.1513)*(((p_1hr-p_wf)/(m))-(np.log10((k*12**2)/(phi*mu*ct*rw**2)))+(3.227))
    return (s)
#Header
l8 = Label(window,text = "Skin Problem")
l8.grid(row = 10,column = 1)
#1st row
l9 = Label(window,text = "Pressure (1hr)")
l9.grid(row = 11,column =0 )
p_1hr = StringVar()
t7 = Entry(window, textvariable = p_1hr)
t7.grid (row=11,column=1)
#2nd row
l10 = Label(window,text = "Pressure (Pwf) =")
l10.grid(row = 12,column =0)
p_wf = StringVar()
t8 = Entry(window, textvariable = p_wf)
t8.grid (row=12,column=1)
#3rd row
l11 = Label(window,text = "Porosity =")
l11.grid(row = 13,column =0 )
phi = StringVar()
t9 = Entry(window, textvariable = phi)
t9.grid (row=13,column=1)
#4th row
l12 = Label(window,text = "Well Bore radious =")
l12.grid(row = 14,column =0 )
rw = StringVar()
t10 = Entry(window, textvariable = rw)
t10.grid (row=14,column=1)
#Button
b3 = Button(window, text = "Skin", command = s)
b3.grid (row=14,column=3)
# =============================================================================
# Productivity index
# =============================================================================
def IP(k,h,mu,Bo,re,rw):
     j = (0.00708*k*h)/(mu*Bo*np.log(re/rw))
     return j
#Header
l8 = Label(window,text = "Skin Problem")
l8.grid(row = 15,column = 1)
#1st row
l11 = Label(window,text = "Permeability =")
l11.grid(row = 16,column =0 )
k = StringVar()
t11 = Entry(window, textvariable = k)
t11.grid (row=16,column=1)
#2nd row
l12 = Label(window,text = "Formation Heigth =")
l12.grid(row = 17,column =0)
h1 = StringVar()
t12 = Entry(window, textvariable = h1)
t12.grid (row=17,column=1)
#3rd row
l13 = Label(window,text = "Viscosity =")
l13.grid(row = 18,column =0 )
mu1 = StringVar()
t13 = Entry(window, textvariable = mu1)
t13.grid (row=18,column=1)
#4th row
l14 = Label(window,text = "Oil Volume Factor =")
l14.grid(row = 19,column =0 )
Bo1 = StringVar()
t14 = Entry(window, textvariable = Bo1)
t14.grid (row=19,column=1)
#5th row
l15 = Label(window,text = "Investigation Radious =")
l15.grid(row = 20,column=0)
re = StringVar()
t15 = Entry(window, textvariable = re)
t15.grid (row=20,column=1)
#6th row
l16 = Label(window,text = "Well Bore radious =")
l16.grid(row = 21,column =0 )
rw1 = StringVar()
t16 = Entry(window, textvariable = rw1)
t6.grid (row=21,column=1)
#Button
b4 = Button(window, text = "Productivity index", command = s)
b4.grid (row=22,column=3)


window.mainloop()

