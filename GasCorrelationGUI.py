# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:49:58 2020

@author: Luis Navarro
"""
import numpy as np
import math
from tkinter import *
import tkinter as tk 


window = Tk()
window.geometry("520x600")

window.title("Correlacion Numerica de Gas")

# =============================================================================
#Encabezados 
image = tk.PhotoImage(file="capture.gif")
image = image.subsample(4,4)
label2 = tk.Label(image=image)
label2.grid(row=0,column=0)

image1 = tk.PhotoImage(file="UNAM.gif")
image1 = image1.subsample(4,4)
label3 = tk.Label(image=image1)
label3.grid(row=0,column=2)
l1 = Label(window,text="Universidad Nacional\t\n Autonoma de Mexico\t\n\nFacultad de Ingenieria\t\n\nIngenieria de Yacimientos de Gas\t")
l1.grid(row=0,column=1)

# Entradas
# =============================================================================
l3 = Label(window,text="Presion Pseudoreducida 'P_sr' :")
l3.grid(row=3,column=0)
p_pr = StringVar()
t1 = Entry(window,textvariable=p_pr)
t1.grid(row=3,column=1)
l4 = Label(window,text="Temperatura Pseudoreducida 'T_sr' :")
l4.grid(row=4,column=0)
t_pr = StringVar()
t2 = Entry(window,textvariable=t_pr)
t2.grid(row=4,column=1)

l15 = Label(window,text=" 0.2 <P_sr<30\n1.05<T_sr<3")
l15.grid(row=8,column=0)

l14 = Label(window,text=" 0.2<P_sr<30 \n 1<T_sr<3")
l14.grid(row=12,column=0)

#"""
def z_DPR():
    p_pr = float(t1.get())
    t_pr = float(t2.get())
    A1 = 0.31506237 ; A2 = -1.0467099 ; A3 = -0.57832720 ; A4 =  0.53530771
    A5 = -0.61232032 ; A6 = -0.10488813 ; A7 = 0.68157001 ; A8 = 0.68446549   
    T1 = A1 + A2 / t_pr + A3 / t_pr**3
    T2 = A4 + A5 / t_pr
    T3 = A5 * A6 / t_pr
    T4 = A7 / t_pr**3
    T5 = 0.27 * p_pr / t_pr  
    tol = 1e-13
    def  f(rho_r):
        f = 1 + T1*rho_r + T2 * rho_r**2 + T3 * rho_r**5 + (T4 * rho_r**2 * (1 + A8 * rho_r**2)) * np.exp(-A8 * rho_r**2) - T5 / rho_r
        return f
    
    def f_prima(rho_r):
        f_prima = T1 + 2 * T2 * rho_r + 5 * T3 * rho_r**4 + 2 * T4 * rho_r * np.exp(-A8 * rho_r**2) * ((1 + 2 * A8 * rho_r**2) - A8 * rho_r**2 * (1 + A8 * rho_r**2)) + T5 / rho_r**2
        return f_prima 
    
    rho_r0 =  0.27 * p_pr / t_pr 
    rho_rk = rho_r0
    i = -1
    while True:
        if (abs(f(rho_rk)) < tol):
            break 
        
        rho_rk1 = rho_rk - f(rho_rk) / f_prima(rho_rk)
        delta = abs(rho_rk-rho_rk1)
        
        if (delta < tol):
            break 
        else:
            rho_rk = rho_rk1
            i = i+1
    z = 0.27 * p_pr / (rho_rk * t_pr)
    l6 =Label(text=z)
    l6.grid(row=7,column=1)
    l7 =Label(text=rho_rk)
    l7.grid(row=9,column=1)
    
def z_DAK():
    p_pr = float(t1.get())
    t_pr = float(t2.get()) 
    e = 1e-15    
    rho_r = (0.27*p_pr)/t_pr
    while True:
        A1 = 0.3265 ; A2 = -1.0700 ; A3 = -0.5339 ;  A4 = 0.01569 ; A5 = -0.05165
        A6 = 0.5475 ; A7 = -0.7361 ; A8 = 0.1844 ; A9 = 0.1056 ; A10 = 0.6134  ; A11 = 0.7210
        R1 = A1 + A2/t_pr + A3/t_pr**3 + A4/t_pr**4 + A5/t_pr**5
        R2 = (0.27*p_pr)/t_pr
        R3 = A6 + A7/t_pr + A8/t_pr**2 
        R4 = A9*(A7/t_pr+A8/t_pr**2)
        R5 = A10 / t_pr**3
        f = R1*rho_r - R2/rho_r + R3*rho_r**2 - R4*rho_r**5 + A10*(1+A11*rho_r**2)*((rho_r**2)/(t_pr**3))*math.exp(-A11*rho_r)
        f_prima = R1+R2/rho_r**2 + 2*R3*rho_r - 5*(R4)*rho_r**4 + 2*(R5)*rho_r*math.exp(-A11*rho_r)*((1+2*A11*rho_r**3)-A11*rho_r**2*(1+A11*rho_r**2))
        rho_n = rho_r -f/f_prima
        error = abs(rho_n-rho_r)
        if error < e:
            break
            
        rho_r = rho_n
        z = (0.27*p_pr)/(rho_r*t_pr)
    l12 =Label(text=z)
    l12.grid(row=11,column=1)
    l13 =Label(text=rho_r)
    l13.grid(row=13,column=1)
#"""
    
# =============================================================================
# Botones
# =============================================================================
l5 = Label(window,text='- Calculo de "z" y "ρ_r" -')
l5.grid(row= 5,column=1 )
b1 = Button(window,text ="DPR", command = z_DPR)
b1.grid(row= 7,column=0 )
b2 = Button(window,text ="DAK",command = z_DAK)
b2.grid(row= 11,column=0 )
# =============================================================================
# Resultados
# =============================================================================
l8 = Label(window, text ="Factor de desviacion:")
l8.grid(row=6,column=1) 
l9 = Label(window, text ="Densidad reducida:")
l9.grid(row=8,column=1)
l10 = Label(window, text ="Factor de desviacion:")
l10.grid(row=10,column=1) 
l11 = Label(window, text ="Densidad reducida:")
l11.grid(row=12,column=1)
# =============================================================================
# Factor de COmpresibilidad isotermica
def cg():
    p_pr = float(t1.get())
    t_pr = float(t2.get())
    z = float(t4.get())
    rho_r = float(t5.get())
    p_pc = float(t3.get())
    A1 = 0.31506237 ; A2 = -1.0467099 ; A3 = -0.57832720 ; A4 =  0.53530771 ; A5 = -0.61232032
    A6 = -0.10488813 ; A7 = 0.68157001 ; A8 = 0.68446549
    
    dz_drho = A1 + A2/t_pr + A3/t_pr**3 + 2*(A4 + A5/t_pr)*rho_r + 5*A5*A6*(rho_r**4/t_pr) + (((2*A7*rho_r)/(t_pr**3))*(1+A8*rho_r**2-(A8*rho_r**2)**2)*np.exp(-A8*rho_r**2))
    
    c_r = 1/p_pr - (0.27/(z**2*t_pr))*((dz_drho)/(1+(rho_r/z)*(dz_drho)))
    
    c_g = c_r/p_pc
    cg = c_g *10**6

    l22 =Label(text=cg)
    l22.grid(row=18,column=1)
    l23 = Label(text="x10^(-6) [psi^-1]")
    l23.grid(row=18,column=2)
    
l19 = Label(window,text="- Calculo de Compresibilidad Isotermica -")
l19.grid(row=14,column=1)
l20 = Label(window,text="Presion Pseudocritica 'P_pc' :")
l20.grid(row=15,column=0)
l21 = Label(window,text="[psi]")
l21.grid(row=15,column=2)
p_pc = StringVar()
t3 = Entry(window,textvariable=p_pc)
t3.grid(row=15,column=1)
l22 = Label(window,text="Factor de desviacion 'z' : ")
l22.grid(row=16,column=0)
z_cg = StringVar()
t4 = Entry(window,textvariable=z_cg)
t4.grid(row=16,column=1)
l23 = Label(window,text="Densidad reducida 'ρ_r' : ")
l23.grid(row=17,column=0)
rho_cg = StringVar()
t5 = Entry(window,textvariable=rho_cg)
t5.grid(row=17,column=1)
b3 = Button(window,text ="Calcular", command = cg)
b3.grid(row= 18,column=0 )
# =============================================================================
# =============================================================================
# Factor Volumetrico de Gas
# =============================================================================
def B_g():
    p = float(t6.get())
    T = float(t7.get())
    z = float(t8.get())
    Bg = 0.02827*((z*(T+459.67))/(p))
    
    l34 =Label(text=Bg)
    l34.grid(row=23,column=1)
    l35 = Label(text="[ft^3/scf]")
    l35.grid(row=23,column=2)
    
l30 = Label(window,text="- Calculo de Factor Volumetrico de Gas -")
l30.grid(row=19,column=1)
l31 = Label(window,text="Presion 'P' :")
l31.grid(row=20,column=0)
p_bg = StringVar()
t6 = Entry(window,textvariable=p_bg)
t6.grid(row=20,column=1)
l32 = Label(window,text="[psi]")
l32.grid(row=20,column=2)
l31 = Label(window,text="Temperatura 'T' :")
l31.grid(row=21,column=0)
t_bg = StringVar()
t7 = Entry(window,textvariable=t_bg)
t7.grid(row=21,column=1)
l32 = Label(window,text="[°F]")
l32.grid(row=21,column=2)
l33 = Label(window,text="Factor de desviacion 'z' :")
l33.grid(row=22,column=0)
z_bg = StringVar()
t8 = Entry(window,textvariable=z_bg)
t8.grid(row=22,column=1)
b4 = Button(window,text ="Calcular", command = B_g)
b4.grid(row= 23,column=0 )
# =============================================================================
# creditos 
def buttonClick():
    tk.messagebox.showinfo('Creditos', 'Profesor: Dr.Victor Arana\nEstudiantes:\nLuis Enrique Navarro Morales\nHugo Cesar Mondragon Basurto\nLuis Antonio Dominguez Alejo\nEric Javier Trejo Rodriguez')
b5 = Button(window,text ="Creditos",command = buttonClick)
b5.grid(row= 25,column=2 )
# =============================================================================


window.mainloop()