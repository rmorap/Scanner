import pandas as pd
import re
import codecs
import os
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename 
from tkinter import messagebox

messagebox.showinfo(message="Seleccione archivo con tokens", title="Tokens")
filename = askopenfilename()
dir_t = filename
print('\n'+'Has escogido: '+ filename+'\n')
with open(dir_t, 'r') as archivo:
    separador = ':'
    data = {}
    
    for linea in archivo:
        key, value = linea.split(separador)
        data[key.strip()] = value.strip()

print(data)
messagebox.showinfo(message="Seleccione archivo python", title="Codigo Python")
filename = askopenfilename()
dir_t = filename
print('\n'+'Has escogido: '+ filename+'\n')
fp = codecs.open(dir_t,"r","utf-8")
cadena = fp.read()
fp.close()
cadena_real = cadena.split('\n')
cadena_c = []
for i in range(len(cadena_real)):
    cadena_c += cadena_real[i].split(' ')
print(cadena_c)
tokens = []
for j in range(len(cadena_c)):
    for k,v in data.items():
        for m in re.finditer(v, cadena_c[j]):
            l =  m.group(0)
            tokens.append(l+', '+k)

for i in range(len(tokens)):
    print(tokens[i])