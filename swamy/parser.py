import ply.yacc as yacc
from lexer import tokens

# Define the starting symbol
# start = 'array_declaration'

# Grammar rules
def p_function_declaration(p):
    '''function_declaration : FUNCTION ID LPAREN parameters RPAREN exp return END'''

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

def p_empty(p):
    '''empty : '''

def p_string(p):
    '''string : SQ ID SQ
              | DQ ID DQ'''

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
function nigger(a,b,c)
    a=b+a;
    return "a@"
end
'''
try:
    result = parser.parse(input_declaration)
    print("No syntax error")
except Exception as e:
    print(e)
