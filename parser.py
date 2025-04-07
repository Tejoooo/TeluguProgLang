from ast_nodes import *

def parse(tokens):
    pos = 0
    ast = []

    def peek():
        if pos >= len(tokens):
            return ('EOF', '')
        return tokens[pos]

    def advance():
        nonlocal pos
        if pos < len(tokens):
            tok = tokens[pos]
            pos += 1
            return tok
        else:
            raise IndexError("No more tokens available.")    
        
    def expect(expected_type):
        token = advance()
        if token[0] != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token}")
        return token
    
    def parse_expression():
        nonlocal pos
        left_type, left_val = advance()
        # Parse the left operand (either a number or a variable)
        if left_type == 'NUMBER':
            left = Number(left_val)
        elif left_type == 'STRING':
            left = String(left_val[1:-1])
        elif left_type == 'ID':
            if pos < len(tokens) and tokens[pos][0] == 'LPAREN':
        # It's a function call!
                advance()  # Skip '('
                args = []
                while tokens[pos][0] != 'RPAREN':
                    args.append(parse_expression())
                    if tokens[pos][0] == 'COMMA':
                        advance()  # Skip ','
                advance()  # Skip ')'
                left = FunctionCall(left_val, args)
            else:
                left = Var(left_val)
        else:
            raise SyntaxError("Expected a number or variable")

        while pos < len(tokens) and tokens[pos][0] in ('LE', 'LT', 'GT', 'GE', 'EQ', 'NE'):
            op_type, op_val = advance()  # Get the comparison operator
            right_type, right_val = advance()
        
        # Parse the right operand (either a number or a variable)
            if right_type == 'NUMBER':
                right = Number(right_val)
            elif right_type == 'STRING':
                right = String(right_val)
            elif right_type == 'ID':
                right = Var(right_val)
            else:
                raise SyntaxError("Expected a number or variable after operator")
        
        # Create a BinaryOp node combining the left operand, operator, and right operand
            left = BinaryOp(left, op_val, right)
    
    # Parse arithmetic operations (addition, subtraction, multiplication, division)
        while pos < len(tokens) and tokens[pos][0] in ('PLUS', 'MINUS', 'STAR', 'SLASH'):
            op_type, op_val = advance()
            right_type, right_val = advance()
        
            if right_type == 'NUMBER':
                right = Number(right_val)
            elif right_type == 'ID':
                right = Var(right_val)
            else:
                raise SyntaxError("Expected a number or variable after operator")
        
        # Combine the left operand with the operator and the right operand
            left = BinaryOp(left, op_val, right)

        return left


    def parse_block():
        nonlocal pos
        block = []
        if tokens[pos][0] not in ('LOPALA', 'లోపల'):
            raise SyntaxError("Expected 'lopala' to start block")
        pos += 1  # Skip 'lopala'
        while tokens[pos][0] not in ('AAPEY', 'ఆపే'):
            kind, _ = peek()
            # print(kind)
            if kind == 'viluva' or kind == 'విలువ':
                advance()
                _, name = advance()
                advance()  # '='
                expr = parse_expression()
                advance()  # ';'
                block.append(LetStatement(name, expr))
            elif kind == 'RAAYI' or kind =='రాయీ':
                advance()
                expr = parse_expression()
                advance()  # ';'
                block.append(PrintStatement(expr))
            elif kind == 'LOOPU' or kind == 'లూప్':
                # print("ins")
                advance()
                condition = parse_expression()
                body = parse_block()
                block.append(WhileLoop(condition, body))
            elif kind == 'KOSAM' or kind == 'కోసం':
                block.append(parse_kosam_loop())
            elif kind == 'ID':
                name = advance()[1]  # Get variable name
                # print("his")
                if peek()[0] == 'EQUALS':
                    # print("hi")
                    advance()  # Skip '='
                    expr = parse_expression()
                    expect('SEMICOLON')  # Expect ';'
                    block.append(LetStatement(name, expr))  # Single assignment statement
                elif peek()[0] == 'LPAREN':
        # It's a function call

                    pos -= 1  # Step back so full expression is parsed
                    expr = parse_expression()
                    expect('SEMICOLON')
                    block.append(ExpressionStatement(expr))
                else:
                    raise SyntaxError(f"Unexpected token after identifier: {peek()}")
            elif kind == 'PAMPINCHU' or kind == 'పంపించు':
                advance()  # Skip 'pampinchu'
                expr = parse_expression()
                expect('SEMICOLON')
                block.append(ReturnStatement(expr))
            else:
                raise SyntaxError(f"Unknown statement inside block: {kind}")
        pos += 1  # Skip 'aapey'
        return block

    def parse_kosam_loop():
        nonlocal pos
        advance()  # 'kosam'
        _, var_name = advance()  # loop variable
        advance()  # '='
        start_expr = parse_expression()
        advance()  # 'to'
        end_type, end_val = advance()
        if end_type == 'NUMBER':
            end_expr = Number(end_val)
        elif end_type == 'ID':
            end_expr = Var(end_val)
        else:
            raise SyntaxError("Invalid end value in for loop")
        body = parse_block()
        # print(body)
        return ForLoop(var_name, start_expr, end_expr, body)
    
    def parse_loopu_while():
        nonlocal pos
        advance() 
        condition = parse_expression()  
        # print("While condition:", condition)
        # print("by")
        body = parse_block()  
        # print("While body:", body)

        return WhileLoop(condition, body)

    def parse_srushtinchu():
        nonlocal pos

        advance()  # Skip 'SRUSHTINCHU'
        _, name = advance()  # Function name

        expect("LPAREN")  # (
        params = []

        while peek()[0] != "RPAREN":
            _, param = expect("ID")
            params.append(param)
            if peek()[0] == "COMMA":
                advance()  # skip comma

        expect("RPAREN")  # )
        body = parse_block()
        return FunctionDef(name, params, body)
  
    def parse_if_else():
        global pos
        pos += 1  # Skip 'ITEY'
        condition = parse_expression()

        if tokens[pos][0] == 'LOPALA' or tokens[pos][0] == 'లోపల':  # 'LOPALA' means 'begin'
            pos += 1
        if_body = []
        while tokens[pos][0] != 'MUGIMPU' or tokens[pos][0] != 'ముగింపు':
            if_body.append(parse_block())
        pos += 1  # Skip 'MUGIMPU'

        else_body = []
        if pos < len(tokens) and tokens[pos][0] == 'LEKAPOTE' or tokens[pos][0] != 'లేకపోతె':
            pos += 1
            if tokens[pos][0] == 'LOPALA' or tokens[pos][0] == 'లోపల':
                pos += 1
            while tokens[pos][0] != 'MUGIMPU' or tokens[pos][0] != 'ముగింపు':
                else_body.append(parse_block())
            pos += 1  # Skip 'MUGIMPU'

        return IfElseStatement(condition, if_body, else_body)
    
    while pos < len(tokens) and tokens[pos][0] not in ('MODALLU','మొదలు'):
        pos += 1

    if pos >= len(tokens):
        raise SyntaxError("Program must start with 'modallu'")
    pos += 1  # Skip 'modallu'

    # Main body parsing
    while pos < len(tokens) and tokens[pos][0] not in ('MUGIMPU','ముగింపు'):
        kind, _ = peek()
        # print(kind)
        if kind == 'VILUVA' or kind == 'విలువ':
            advance()
            _, name = advance()
            advance()  # '='
            expr = parse_expression()
            advance()  # ';'
            ast.append(LetStatement(name, expr))
        elif kind == 'RAAYI' or kind == 'రాయీ':
            advance()
            expr = parse_expression()
            advance()  # ';'
            ast.append(PrintStatement(expr))
        elif kind == 'LOOPU' or kind == 'లూప్':
            # print("hi")
            ast.append(parse_loopu_while())
        elif kind == 'KOSAM' or kind == 'కోసం':
            ast.append(parse_kosam_loop())
        elif kind == 'SRUSHTINCHU' or kind == 'సృష్టించు':
            ast.append(parse_srushtinchu())
        elif kind == 'ITEY' or kind == 'ఇతే':
            ast.append(parse_if_else())
        elif kind == 'ID':
    # Might be a function call or assignment
            name = advance()[1]  # Consume identifier
            if peek()[0] == 'EQUALS':
                advance()  # Consume '='
                expr = parse_expression()
                expect('SEMICOLON')
                ast.append(LetStatement(name, expr))  # Assignment
            elif peek()[0] == 'LPAREN':
        # Function call or expression
                pos -= 1  # Step back so parse_expression() gets the full function call
                expr = parse_expression()
                expect('SEMICOLON')
                ast.append(ExpressionStatement(expr))  # Expression like `add(10, 20);`
        else:
            raise SyntaxError(f"Unknown top-level statement: {kind}")

    return ast
