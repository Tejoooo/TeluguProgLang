from ast_nodes import *
import ast_nodes


class Interpreter:
    def __init__(self):
        self.env = {}

    def eval(self, ast):
        for stmt in ast:
            if isinstance(stmt, LetStatement):
                self.env[stmt.name] = self.eval_expr(stmt.value)
            elif isinstance(stmt, PrintStatement):
                value = self.eval_expr(stmt.expr)
                print(value)
            elif isinstance(stmt, WhileLoop):
                # print(stmt.condition)
                while self.eval_expr(stmt.condition):
                    for s in stmt.body:
                        self.eval_stmt(s)
            elif isinstance(stmt, ForLoop):
                start = self.eval_expr(stmt.start_expr)
                end = self.eval_expr(stmt.end_expr)
                for i in range(start, end + 1):
                    self.env[stmt.var_name] = i
                    for s in stmt.body:
                        self.eval_stmt(s)
            elif isinstance(stmt, FunctionDef):
                # Store the function in the environment
                self.env[stmt.name] = stmt
            elif isinstance(stmt, FunctionCall):
                # print("inhre")
                self.eval_function_call(stmt) 
            elif isinstance(stmt, IfElseStatement):
                if self.eval_expr(stmt.condition):
                    for s in stmt.then_branch:
                        self.eval_stmt(s)
                elif stmt.else_branch:
                    for s in stmt.else_branch:
                        self.eval_stmt(s)

    def eval_stmt(self, stmt):
        
        if isinstance(stmt, LetStatement):
            self.env[stmt.name] = self.eval_expr(stmt.value)
        elif isinstance(stmt, PrintStatement):
            print(self.eval_expr(stmt.expr))
        elif isinstance(stmt, WhileLoop):
            while self.eval_expr(stmt.condition):
                for s in stmt.body:
                    self.eval_stmt(s)
        elif isinstance(stmt, IfElseStatement):
            if self.eval_expr(stmt.condition):
                for s in stmt.then_branch:
                    self.eval_stmt(s)
            elif stmt.else_branch:
                for s in stmt.else_branch:
                    self.eval_stmt(s)
        elif isinstance(stmt, ForLoop):
            start = self.eval_expr(stmt.start_expr)
            end = self.eval_expr(stmt.end_expr)
            for i in range(start, end + 1):
                self.env[stmt.var_name] = i
                for s in stmt.body:
                    self.eval_stmt(s)
        elif isinstance(stmt, FunctionCall):
            # print("hell")
            # Handle function calls
            func = self.env.get(stmt.name)
            if not func:
                raise RuntimeError(f"Function {stmt.name} not defined")

            if len(func.params) != len(stmt.arguments):
                raise RuntimeError(f"Function {stmt.name} called with incorrect number of arguments")

            # Create a new environment for the function call
            local_env = self.env.copy()
            for param, arg in zip(func.params, stmt.arguments):
                local_env[param] = self.eval_expr(arg)
            original_env = self.env
            self.env = local_env

            # Execute the function's body with the new environment
            try:
                for s in func.body:
                    self.eval_stmt(s)
            except ReturnException as e:
                self.env=original_env
                return e.value
            finally:
                self.env = original_env
            # Execute the function's body with the new environment
            return None
        elif isinstance(stmt, ReturnStatement):
            value = self.eval_expr(stmt .expr)
            raise ReturnException(value)

    def eval_expr(self, expr):

        if isinstance(expr, Number):
            return expr.value
        elif isinstance(expr, String):
            return expr.value
        elif isinstance(expr, Var):  # ✅ Updated
            return self.env.get(expr.name, f"undefined({expr.name})")
        elif isinstance(expr, BinaryOp):  # ✅ Updated
            left = self.eval_expr(expr.left)
            right = self.eval_expr(expr.right)
            if expr.op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif expr.op == '-':
                return left - right
            elif expr.op == '*':
                return left * right
            elif expr.op == '/':
                return left // right  # use integer division
            elif expr.op == '<':
                return left < right
            elif expr.op == '<=':
                return left <= right
            elif expr.op == '>':
                return left > right
            elif expr.op == '>=':
                return left >= right
            elif expr.op == '==':
                return left == right
            elif expr.op == '!=':
                return left != right    
        elif isinstance(expr, ast_nodes.FunctionCall):
            # Handle function call expression evaluation
            # print(expr)
            func = self.env.get(expr.name)
            if not func:
                raise RuntimeError(f"Function {expr.name} not defined")

            if len(func.params) != len(expr.args):
                raise RuntimeError(f"Function {expr.name} called with incorrect number of arguments")

            # Create a new environment for the function call
            local_env = self.env.copy()
            for param, arg in zip(func.params, expr.args):
                local_env[param] = self.eval_expr(arg)

            original_env = self.env
            self.env = local_env

            # Execute the function's body with the new environment
            try:
                for s in func.body:
                    self.eval_stmt(s)
            except ReturnException as e:
                self.env=original_env
                return e.value
            finally:
                self.env = original_env
            return None
        else:
            raise RuntimeError(f"Unknown expression type: {type(expr)}")
