import ply.lex as lex
import re
import codecs
from os.path import dirname, join
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename

reservadas = ['HELP','ASYNC','AWAIT','AND','OR','AS','ASSERT','BREAK'
'CLASS','CONTINUE','DEF','DEL','FOR','FROM','GLOBAL','IF','ELIF','ELSE',
'IMPORT','IN','IS','NOT','PASS','PRINT','RETURN','TRUE','FALSE','NONE',
'WHILE']
tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
'ASSIGN','NE','LT','LTE','GT','GTE','LPARENT', 'RPARENT','COMMA',
'COLON','SEMMICOLOM','DOT','UPDATE','REAL']


cd = dirname(__file__)
path = join(cd, "./tokens.txt")
f = open(path, 'r')
while(True):
    linea = f.readline()
    linea = linea.strip()
    if(linea == r'\+'):
        t_PLUS = r'\+'
        print(linea)
    elif(linea == r'\d+\.\d'):
        def t_REAL(t):
            r'\d+'
            return t
    elif(linea == r'='):
        t_ASSIGN = r'='
    elif(linea == r'\d+'):
        def t_NUMBER(t):
            r'\d+'
            return t
    elif(linea == r'[a-zA-Z_][a-zA-Z0-9_]*'):
        def t_ID(t):
            r'[a-zA-Z_][a-zA-Z0-9_]*'
            if t.value.upper() in reservadas:
                t.value = t.value.upper()
            return t

    elif(linea == '\-'):
        t_MINUS = r'\-'
    elif(linea == '\*'):
        t_TIMES = '\*'
    elif(linea == r'/'):
        t_DIVIDE = r'/'
    elif(linea == r'<>'):
        t_NE = r'<>'
    elif(linea == r'<'):
        t_LT = r'<'
    elif(linea == r'<='):
        t_LTE = r'<='
    elif(linea == r'>'):
        t_GT = r'>'
    elif(linea == r'>='):
        t_GTE = r'>='
    if(linea == r'\('):
        t_LPARENT = r'\('
    elif(linea == r'\)'):
        t_RPARENT = r'\)'
    elif(linea == r','):
        t_COMMA = r','
    elif(linea == r':'):
        t_COLON = r':'
    elif(linea == r';'):
        t_SEMMICOLOM = r';'
    elif(linea == r'\.'):
        t_DOT = r'\.'
    elif(linea == r':='):
        t_UPDATE = r':='
    elif(linea == r'\n+'):
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)
    elif(linea == r'\#.*'):
        def t_COMMENT(t):
            r'\#.*'
            pass
    elif(linea == r'\s'):
        def t_WhiteSpaces(t):
            r'\s'
            t.value = str(t.value)
            pass
    if not linea:
        break
f.close()





def t_error(t):
	print("caracter ilegal"+t.value[0])
	t.lexer.skip(1)





raiz = Tk()
raiz.title('Scanner')
raiz.resizable(0,0)
filename = askopenfilename()
dir_t = filename
print('\n'+'Has escogido: '+ filename+'\n')
fp = codecs.open(dir_t,"r","utf-8")
cadena = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok:break
	print(tok)
