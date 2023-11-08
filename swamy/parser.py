import ply.yacc as yacc
from lexer import tokens

# Define the starting symbol
# start = 'array_declaration'

# Grammar rules

def p_command(p):
    '''command : exp
               | function_declaration
               | array_declaration
               | if
               '''

def p_function_declaration(p):
    '''function_declaration : FUNCTION ID LPAREN parameters RPAREN exp return END
                            | FUNCTION ID LPAREN parameters RPAREN empty return END'''


def p_return(p):
    '''return : RETURN parameters
              | RETURN exp
              | RETURN string'''


def p_parameters(p):
    '''parameters : empty
                  | parameter
                  | parameters COMMA parameter'''

def p_parameter(p):
    '''parameter : ID'''

def p_array_declaration(p):
    '''array_declaration : ID ASSIGN LFLOWER elements RFLOWER'''

def p_elements(p):
    '''elements : empty
                | element
                | elements COMMA element'''

def p_element(p):
    '''element : ID
               | NUMBER '''

def p_string(p):
    '''string : SQ ID SQ
              | DQ ID DQ
              | SQ empty SQ
              | DQ empty DQ'''

def p_if(p):
    '''if : IF exp THEN exp else END'''

def p_else(p):
    '''else : empty
            | ELSE exp'''

def p_empty(p):
    '''empty : '''

def p_exp(p):
    '''exp : NUMBER
           | ID
           | exp AND exp
           | exp OR exp
           | NOT exp
           | exp ADD exp
           | exp MINUS exp
           | exp MULTIPLY exp
           | exp DIVIDE exp
           | exp LT exp
           | exp LTE exp
           | exp GT exp
           | exp GTE exp
           | exp EQUAL exp
           | exp NE exp
           | ID ASSIGN exp
           | LPAREN exp RPAREN'''


# Error handling rule
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Define the input declaration
input_declaration = '''
if a==b then
    a=c
else
    b=c
end
'''
try:
    result = parser.parse(input_declaration)
    print("No syntax error")
except Exception as e:
    print(e)
