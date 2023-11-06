import ply.lex as lex

# List of token names
tokens = (
    'ID',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'NUMBER',
    'ASSIGN',
    'FUNCTION',
    'END',
    'RETURN',
    'EQUAL',
    'NE',
    'LT',
    'GT',
    'LTE',
    'GTE',
    'ADD',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'AND',
    'OR',
    'NOT',
    'SQ',
    'DQ',
)

# Regular expression rules for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_NUMBER = r'\d+'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_NE = r'\!='
t_LT = r'\<'
t_GT = r'\>'
t_LTE = r'\<='
t_GTE = r'\>='
t_ADD = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_SQ = r'\''
t_DQ = r'\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
        'do'    : 'DO',
        'else'  : 'ELSE',
        'while' : 'WHILE',
        'then'  : 'THEN',
        'end'   : 'END',
        'if'    : 'IF',
        "return":"RETURN",
        "function":"FUNCTION",
        "end":"END",
        'and' : 'AND',
        'or' : 'OR',
        'not' : 'NOT'
    }
    t.type = keywords.get(t.value, "ID")
    return t

t_ignore = ' \t\n@#$%&`;'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
