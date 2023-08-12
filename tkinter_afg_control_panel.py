# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:42:44 2023

@author: Vikram Venkidu
"""

import tkinter as tk

root=tk.Tk()

for i in range(0,10):
    for j in range(0,10):
        label=tk.Label(root,text="").grid(column=i,row=j, padx=10, pady=10)

sin_label=tk.Label(root,text="x").grid(column=1,row=1)
squ_label=tk.Label(root,text="x").grid(column=1,row=2)
ramp_label=tk.Label(root,text="x").grid(column=1,row=3)
def sin_pressed():
    
    tk.Label(root,text="o").grid(column=1,row=2)
    tk.Label(root,text="o").grid(column=1,row=3)
    

tk.Button(root, text="Sine", command=sin_pressed).grid(column=2,row=1)
tk.Button(root, text="Square", command=sample_command).grid(column=2,row=2)
tk.Button(root, text="Ramp", command=sample_command).grid(column=2,row=3)




#    if user_input:
#        freqlabel.config(text=user_input+'Hz')

DC_entry=tk.Entry(root)
DC_entry.grid(column=2,row=5)

tk.Label(root, text="DC Offset[V]").grid(column=1, row=5)

Amp_entry=tk.Entry(root)
Amp_entry.grid(column=2,row=6)
tk.Label(root, text="Amplitude[V]").grid(column=1, row=6)

Freq_entry=tk.Entry(root)
Freq_entry.grid(column=2, row=7)
tk.Label(root, text="Frequency[Hz]").grid(column=1, row=7)

Phi_entry=tk.Entry(root)
Phi_entry.grid(column=2,row=8)
tk.Label(root, text="Phi[deg]").grid(column=1, row=8)

def OK_clicked():
    DC_input= DC_entry.get()
    Amp_input= Amp_entry.get()
    Freq_input= Freq_entry.get()
    Phi_input= Phi_entry.get()
    user_input=DC_input or Amp_input or Freq_input or Phi_input
    if user_input: 
        print(DC_input, Amp_input, Freq_input, Phi_input)

tk.Button(root, text="OK", command=OK_clicked).grid(column=8,row=8)

root.mainloop()