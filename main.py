# main.py
import argparse
from lexer import build_lexer
from parser import build_parser
from meu_ast import ast_to_dict
import json

def run_file(path, show_tokens=False):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    lexer = build_lexer()
    parser = build_parser()
    if show_tokens:
        lexer.input(data)
        for tok in lexer:
            print(tok)
        return
    result = parser.parse(data, lexer=lexer)
    print(json.dumps(ast_to_dict(result), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument('file', help='arquivo .c para analisar')
    arg.add_argument('--tokens', action='store_true', help='somente listar tokens')
    args = arg.parse_args()
    run_file(args.file, show_tokens=args.tokens)
