# parser.py
import ply.yacc as yacc
from lexer import tokens, build_lexer
from meu_ast import *

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','EQ','NE'),
    ('left','LT','LE','GT','GE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MOD'),
    ('right','NOT'),
)

start = 'program'

def p_program(p):
    'program : external_list'
    p[0] = Program(p[1])

def p_external_list_empty(p):
    'external_list : '
    p[0] = []

def p_external_list(p):
    'external_list : external_list external_declaration'
    p[0] = p[1] + [p[2]]

def p_external_declaration_declaration(p):
    'external_declaration : declaration'
    p[0] = p[1]

def p_external_declaration_function(p):
    'external_declaration : function_def'
    p[0] = p[1]

def p_declaration(p):
    'declaration : type_specifier init_declarator_list SEMICOLON'
    decls = []
    for name, init in p[2]:
        decls.append(VarDecl(p[1], name, init))
    p[0] = decls if len(decls) > 1 else decls[0]

def p_init_declarator_list_single(p):
    'init_declarator_list : init_declarator'
    p[0] = [p[1]]

def p_init_declarator_list(p):
    'init_declarator_list : init_declarator_list COMMA init_declarator'
    p[0] = p[1] + [p[3]]

def p_init_declarator_id(p):
    'init_declarator : IDENTIFIER'
    p[0] = (p[1], None)

def p_init_declarator_init(p):
    'init_declarator : IDENTIFIER ASSIGN expression'
    p[0] = (p[1], p[3])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR_TYPE
                      | VOID'''
    p[0] = p[1]

def p_function_def(p):
    'function_def : type_specifier IDENTIFIER LPAREN param_list_opt RPAREN compound_stmt'
    p[0] = FunctionDef(p[1], p[2], p[4], p[6])

def p_param_list_opt_empty(p):
    'param_list_opt : '
    p[0] = []

def p_param_list_opt(p):
    'param_list_opt : param_list'
    p[0] = p[1]

def p_param_list_single(p):
    'param_list : param'
    p[0] = [p[1]]

def p_param_list(p):
    'param_list : param_list COMMA param'
    p[0] = p[1] + [p[3]]

def p_param(p):
    'param : type_specifier IDENTIFIER'
    p[0] = VarDecl(p[1], p[2])

def p_compound_stmt(p):
    'compound_stmt : LBRACE stmt_list RBRACE'
    p[0] = Compound(p[2])

def p_stmt_list_empty(p):
    'stmt_list : '
    p[0] = []

def p_stmt_list(p):
    'stmt_list : stmt_list statement'
    p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression_stmt
                 | compound_stmt
                 | selection_stmt
                 | iteration_stmt
                 | return_stmt
                 | declaration'''
    p[0] = p[1]

def p_expression_stmt(p):
    'expression_stmt : expression_opt SEMICOLON'
    p[0] = p[1]

def p_expression_opt_empty(p):
    'expression_opt : '
    p[0] = None

def p_expression_opt(p):
    'expression_opt : expression'
    p[0] = p[1]

def p_selection_stmt_if(p):
    'selection_stmt : IF LPAREN expression RPAREN statement'
    p[0] = If(p[3], p[5])

def p_selection_stmt_if_else(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
    p[0] = If(p[3], p[5], p[7])

def p_iteration_stmt_while(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    p[0] = While(p[3], p[5])

def p_iteration_stmt_for(p):
    'iteration_stmt : FOR LPAREN expression_opt SEMICOLON expression_opt SEMICOLON expression_opt RPAREN statement'
    p[0] = For(p[3], p[5], p[7], p[9])

def p_return_stmt(p):
    'return_stmt : RETURN expression_opt SEMICOLON'
    p[0] = Return(p[2])

def p_expression(p):
    'expression : assignment_expression'
    p[0] = p[1]

def p_assignment_expression_simple(p):
    'assignment_expression : logical_or_expression'
    p[0] = p[1]

def p_assignment_expression_assign(p):
    'assignment_expression : logical_or_expression ASSIGN assignment_expression'
    p[0] = BinOp('=', p[1], p[3])

def p_logical_or(p):
    'logical_or_expression : logical_and_expression'
    p[0] = p[1]

def p_logical_or_bin(p):
    'logical_or_expression : logical_or_expression OR logical_and_expression'
    p[0] = BinOp('||', p[1], p[3])

def p_logical_and(p):
    'logical_and_expression : equality_expression'
    p[0] = p[1]

def p_logical_and_bin(p):
    'logical_and_expression : logical_and_expression AND equality_expression'
    p[0] = BinOp('&&', p[1], p[3])

def p_equality(p):
    'equality_expression : relational_expression'
    p[0] = p[1]

def p_equality_eq(p):
    'equality_expression : equality_expression EQ relational_expression'
    p[0] = BinOp('==', p[1], p[3])

def p_equality_ne(p):
    'equality_expression : equality_expression NE relational_expression'
    p[0] = BinOp('!=', p[1], p[3])

def p_relational(p):
    'relational_expression : additive_expression'
    p[0] = p[1]

def p_relational_lt(p):
    'relational_expression : relational_expression LT additive_expression'
    p[0] = BinOp('<', p[1], p[3])

def p_relational_gt(p):
    'relational_expression : relational_expression GT additive_expression'
    p[0] = BinOp('>', p[1], p[3])

def p_relational_le(p):
    'relational_expression : relational_expression LE additive_expression'
    p[0] = BinOp('<=', p[1], p[3])

def p_relational_ge(p):
    'relational_expression : relational_expression GE additive_expression'
    p[0] = BinOp('>=', p[1], p[3])

def p_additive(p):
    'additive_expression : multiplicative_expression'
    p[0] = p[1]

def p_additive_plus(p):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    p[0] = BinOp('+', p[1], p[3])

def p_additive_minus(p):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    p[0] = BinOp('-', p[1], p[3])

def p_multiplicative(p):
    'multiplicative_expression : unary_expression'
    p[0] = p[1]

def p_mult_times(p):
    'multiplicative_expression : multiplicative_expression TIMES unary_expression'
    p[0] = BinOp('*', p[1], p[3])

def p_mult_div(p):
    'multiplicative_expression : multiplicative_expression DIVIDE unary_expression'
    p[0] = BinOp('/', p[1], p[3])

def p_mult_mod(p):
    'multiplicative_expression : multiplicative_expression MOD unary_expression'
    p[0] = BinOp('%', p[1], p[3])

def p_unary_primary(p):
    'unary_expression : primary_expression'
    p[0] = p[1]

def p_unary_not(p):
    'unary_expression : NOT unary_expression'
    p[0] = UnaryOp('!', p[2])

def p_unary_plus(p):
    'unary_expression : PLUS unary_expression'
    p[0] = UnaryOp('+', p[2])

def p_unary_minus(p):
    'unary_expression : MINUS unary_expression'
    p[0] = UnaryOp('-', p[2])

def p_primary_identifier(p):
    'primary_expression : IDENTIFIER'
    p[0] = Identifier(p[1])

def p_primary_int(p):
    'primary_expression : INT_CONST'
    p[0] = Literal(p[1])

def p_primary_float(p):
    'primary_expression : FLOAT_CONST'
    p[0] = Literal(p[1])

def p_primary_char(p):
    'primary_expression : CHAR_CONST'
    p[0] = Literal(p[1])

def p_primary_string(p):
    'primary_expression : STRING'
    p[0] = Literal(p[1])

def p_primary_paren(p):
    'primary_expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_primary_call(p):
    'primary_expression : IDENTIFIER LPAREN arg_list_opt RPAREN'
    p[0] = Call(p[1], p[3])

def p_arg_list_opt_empty(p):
    'arg_list_opt : '
    p[0] = []

def p_arg_list_opt(p):
    'arg_list_opt : arg_list'
    p[0] = p[1]

def p_arg_list_single(p):
    'arg_list : expression'
    p[0] = [p[1]]

def p_arg_list(p):
    'arg_list : arg_list COMMA expression'
    p[0] = p[1] + [p[3]]

def p_error(p):
    if p:
        print(f"SyntaxError: linha {p.lineno}, pos {p.lexpos}: token inesperado '{p.value}' (type {p.type})")
        while True:
            tok = parser.token()
            if not tok or tok.type in ('SEMICOLON','RBRACE'):
                break
        parser.errok()
    else:
        print('SyntaxError: EOF reached')

def build_parser(**kwargs):
    global parser
    parser = yacc.yacc(**kwargs)
    return parser

if __name__ == '__main__':
    lexer = build_lexer()
    parser = build_parser()
    data = 'int main() { int a = 0; a = a + 1; return 0; }'
    result = parser.parse(data, lexer=lexer)
    from ast import ast_to_dict
    import json
    print(json.dumps(ast_to_dict(result), indent=2, ensure_ascii=False))
