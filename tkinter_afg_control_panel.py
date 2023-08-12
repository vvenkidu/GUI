# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:42:44 2023

@author: Vikram Venkidu
"""

import tkinter as tk
import pyvisa

# establishing connection
rm= pyvisa.ResourceManager()
resources=rm.list_resources()
print(resources)

visa_address='USB0::0x0699::0x0347::C037742::0::INSTR'
afg=rm.open_resource(visa_address,timeout=10000)
idn=afg.query('*IDN?')
print(idn)


# listing SCPI commands



root=tk.Tk()


# Establish grid skeleton
for i in range(0,10):
    for j in range(0,10):
        label=tk.Label(root,text="").grid(column=i,row=j, padx=10, pady=10)



# Changing function type
sin_command=':SOURce1:FUNCtion:SHAPe SIN'
square_command=':SOURce1:FUNCtion:SHAPe SQU'
ramp_command=':SOURce1:FUNCtion:SHAPe RAMP'

sin_label=tk.Label(root,text="x").grid(column=1,row=1)
squ_label=tk.Label(root,text="x").grid(column=1,row=2)
ramp_label=tk.Label(root,text="x").grid(column=1,row=3)
def sin_pressed():
    tk.Label(root,text="x").grid(column=1,row=1)
    tk.Label(root,text="o").grid(column=1,row=2)
    tk.Label(root,text="o").grid(column=1,row=3)
    afg.write(sin_command)
    

def squ_pressed():
    tk.Label(root,text="o").grid(column=1,row=1)
    tk.Label(root,text="x").grid(column=1,row=2)
    tk.Label(root,text="o").grid(column=1,row=3)
    afg.write(square_command)

def ramp_pressed():
    tk.Label(root,text="o").grid(column=1,row=1)
    tk.Label(root,text="o").grid(column=1,row=2)
    tk.Label(root,text="x").grid(column=1,row=3)
    afg.write(ramp_command)
    

tk.Button(root, text="Sine", command=sin_pressed).grid(column=2,row=1)
tk.Button(root, text="Square", command=squ_pressed).grid(column=2,row=2)
tk.Button(root, text="Ramp", command=ramp_pressed).grid(column=2,row=3)




#    if user_input:
#        freqlabel.config(text=user_input+'Hz')

DC_entry=tk.Entry(root)
DC_entry.grid(column=2,row=5)

tk.Label(root, text="DC Offset[mV]").grid(column=1, row=5)

Amp_entry=tk.Entry(root)
Amp_entry.grid(column=2,row=6)
tk.Label(root, text="Amplitude[VPP]").grid(column=1, row=6)

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
        if DC_input:
            command=':SOURce1:VOLTage:LEVel:IMMediate:OFFSet '+DC_input+'mV'
            afg.write(command)
        if Amp_input:
            command=':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude '+Amp_input+'VPP'
            afg.write(command)
        if Freq_input:
            command=':SOURce1:FREQuency:FIXed '+Freq_input+'HZ'
            afg.write(command)
        if Phi_input:
            command=':SOURce1:PHASe:ADJust '+Phi_input+'DEG'
            afg.write(command)
        print(DC_input, Amp_input, Freq_input, Phi_input)
    
    

tk.Button(root, text="OK", command=OK_clicked).grid(column=8,row=8)

root.mainloop()
