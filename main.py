from lexer import tokenize
from parser import parse
from interpreter import Interpreter

import sys

file_path = sys.argv[1] if len(sys.argv) > 1 else "sample.tl"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

tokens = list(tokenize(code))
ast = parse(tokens)
interpreter = Interpreter()
interpreter.eval(ast)
