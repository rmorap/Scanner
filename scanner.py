import ply.lex as lex
import re
import codecs
import os
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename 

reservadas = ['HELP','ASYNC','AWAIT','AND','OR','AS','ASSERT','BREAK'
'CLASS','CONTINUE','DEF','DEL','FOR','FROM','GLOBAL','IF','ELIF','ELSE',
'IMPORT','IN','IS','NOT','PASS','PRINT','RETURN','TRUE','FALSE','NONE',
'WHILE']
tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
'ASSIGN','NE','LT','LTE','GT','GTE','LPARENT', 'RPARENT','COMMA',
'SEMMICOLOM','DOT','UPDATE']

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("caracter ilegal"+t.value[0])
	t.lexer.skip(1)

def t_WhiteSpaces(t):
    r'\s'
    t.value = str(t.value)
    pass

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

