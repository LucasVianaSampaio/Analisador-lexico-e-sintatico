# lexer.py
import ply.lex as lex

# nomes do tokens
tokens = [
    'IDENTIFIER',
    'INT_CONST', 'FLOAT_CONST', 'CHAR_CONST', 'STRING',
    'PLUS','MINUS','TIMES','DIVIDE','MOD',
    'ASSIGN', 'EQ','NE','LT','LE','GT','GE',
    'AND','OR','NOT',
    'LPAREN','RPAREN','LBRACE','RBRACE','SEMICOLON','COMMA'
]

# palavras chaves
keywords = {
    'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR_TYPE', 'void': 'VOID',
    'if': 'IF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE', 'return': 'RETURN'
}

# adiciona as palvras chaves no tokens
tokens += list(keywords.values())

# regex rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_MOD       = r'%'

t_EQ        = r'=='
t_NE        = r'!='
t_LE        = r'<='
t_LT        = r'<'
t_GE        = r'>='
t_GT        = r'>'

t_ASSIGN    = r'='

t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COMMA     = r','

# ignora spaços e tabs
t_ignore = ' \t\r'

# nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# comentários
def t_comment_multiline(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_comment_single(t):
    r'//.*'
    pass

# identificadores e palavras chaves
def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

# float literal 
def t_FLOAT_CONST(t):
    r'\d+\.\d*|\d*\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        t.value = 0.0
    return t

# integer literal
def t_INT_CONST(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t

# character literal
def t_CHAR_CONST(t):
    r"'([^\\']|\\.)'"
    t.value = t.value[1:-1]
    return t

# string literal
def t_STRING(t):
    r'"([^\\"]|\\.)*"'
    t.value = t.value[1:-1]
    return t

# error handling
def t_error(t):
    print(f"LexicalError: linha {t.lineno}, pos {t.lexpos}: caractere inesperado '{t.value[0]}'")
    t.lexer.skip(1)

def build_lexer(**kwargs):
    return lex.lex(**kwargs)

if __name__ == '__main__':
    lexer = build_lexer()
    data = 'int main() { int a = 5; a = a + 1; }'
    lexer.input(data)
    for tok in lexer:
        print(tok)
