# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:44:29 2023
Testing out the python user interface to build a GUI for controlling multimeters
@author: Vikram Venkidu
"""

import tkinter as tk
import pyvisa

rm= pyvisa.ResourceManager()
resources=rm.list_resources()
print(resources)

visa_address='USB0::0x0699::0x034A::C020262::INSTR'
print(visa_address)
afg=rm.open_resource(visa_address,timeout=10000)

idn=afg.query('*IDN?')
afg.write(':SOURce1:FUNCtion:SHAPe SIN')



root=tk.Tk()
root.title("SOURCE FUNCTION")

label=tk.Label(root,text="SOURCE FUNCTION")
label.pack()




sin_command=':SOURce1:FUNCtion:SHAPe SIN'
square_command=':SOURce1:FUNCtion:SHAPe SQU'
ramp_command=':SOURce1:FUNCtion:SHAPe RAMP'
#pulse_command=':SOURce1:FUNCtion:SHAPe PULS'

def square_button_clicked():
    afg.write(square_command)
    function.config(text="SQUARE")

def sin_button_clicked():
    afg.write(sin_command)
    label.config(text="SIN")

def ramp_button_clicked():
    afg.write(ramp_command)
    label.config(text="RAMP")
    
#def pulse_button_clicked():
#    afg.write(pulse_command)
#    label.config(text="PULSE")

square_button = tk.Button(root, text="square", command=square_button_clicked)
sin_button = tk.Button(root, text="sin", command=sin_button_clicked)
ramp_button = tk.Button(root, text="ramp", command=ramp_button_clicked)
#pulse_button = tk.Button(root, text="pulse", command=pulse_button_clicked)

square_button.pack()
sin_button.pack()
ramp_button.pack()
#pulse_button.pack()



#root.mainloop()

freqroot=tk.Tk()
entry=tk.Entry(freqroot)
tk.Entry()

freqroot.title("Operating Frequency")
freqlabel=tk.Label(freqroot, text="??? Hz")

def freq_button_clicked():
    user_input= entry.get()
    if user_input:
        freq_command=':SOURce1:FREQuency:FIXed '+user_input+'HZ'
        afg.write(freq_command)
        freqlabel.config(text=user_input+'Hz')
        
        
freq_button= tk.Button(freqroot, text="Enter Frequency", command=freq_button_clicked)

entry.pack()
freq_button.pack()
freqroot.mainloop()