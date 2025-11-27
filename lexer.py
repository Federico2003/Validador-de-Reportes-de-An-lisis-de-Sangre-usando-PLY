#importamos librerias
import ply.lex as lex
import re

# Lista de tokens
tokens = (
    'LBRACE', 
    'RBRACE', 
    'LBRACKET',
    'RBRACKET',
    'COLON',
    'COMMA',
    'STRING', 
    'NUMBER'
)

# Tokens simples con expresiones regulares directas
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COLON     = r':'
t_COMMA     = r','

# -------------------------
# STRING: "texto"
# Acepta caracteres normales y escapes tipo \" \n etc.
# -------------------------
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    # quitar comillas
    t.value = t.value[1:-1]
    return t

# -------------------------
# NUMBER: solo enteros (para este proyecto basta)
# -------------------------
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios, tabs y saltos
t_ignore = ' \t\n\r'

# -------------------------
# Manejo de errores léxicos
# -------------------------
def t_error(t):
    print(f"Caracter no permitido: {t.value[0]}")
    t.lexer.skip(1)

# Construir lexer
lexer = lex.lex()

