class LetStatement:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Let({self.name} = {self.value})"

class PrintStatement:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Print({self.expr})"

class String:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'String("{self.value}")'

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"

class WhileLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForLoop:
    def __init__(self, var_name, start_expr, end_expr, body):
        self.var_name = var_name
        self.start_expr = start_expr
        self.end_expr = end_expr
        self.body = body


class FunctionDef:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return f"FunctionDef({self.name}({', '.join(self.params)}) {{ {', '.join(map(str, self.body))} }})"

class IfElseStatement:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch  # list of statements
        self.else_branch = else_branch or []  # list of statements or None

class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class ReturnStatement:
    def __init__(self, expr):
        self.expr = expr
class ExpressionStatement:
    def __init__(self, expr):
        self.expr = expr

class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Var:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
