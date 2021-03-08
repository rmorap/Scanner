import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['HELP','ASYNC','AWAIT','AND','OR','AS','ASSERT','BREAK'
'CLASS','CONTINUE','DEF','DEL','FOR','FROM','GLOBAL','IF','ELIF','ELSE',
'IMPORT','IN','IS','NOT','PASS','PRINT','RETURN','TRUE','FALSE','NONE',
'WHILE']
tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
		'DOT','UPDATE'
		]

#reservadas = {
#	'help':'HELP',
#	'async':'ASYNC',
#	'await': 'AWAIT',
#	'and':'AND',
#	'or':'OR',
#	'as':'AS',
#	'assert':'ASSERT',
#	'break':'BREAK',
#	'class':'CLASS',
#	'continue':'CONTINUE',
#	'def':'DEF',
#	'del':'DEL',
#	'for':'FOR',
##	'from':'FROM',
#	'global':'GLOBAL',
#	'if':'IF',
#	'elif':'ELIF',
#	'else':'ELSE',
#	'import':'IMPORT',
#	'in':'IN',
#	'is':'IS',
#	'not':'NOT',
#	'pass':'PASS',
#	'print':'PRINT',
#	'return':'RETURN',
#	'true':'TRUE',
#	'false':'FALSE',
#	'none':'NONE',
#	'while':'WHILE'
#}

#tokens = tokens+list(reservadas.values())

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

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1
	
	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)
	for file in files:
		print(str(cont)+". "+file)
		cont = cont + 1
	while respuesta == False:
		numArchivo = input('\n Numero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break
	print('Has escogido \'%s\' \n' %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = 'directorio/'
archivo = buscarFicheros(directorio)
dir_t = directorio+archivo
fp = codecs.open(dir_t,"r","utf-8")
cadena = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok:break
	print(tok)