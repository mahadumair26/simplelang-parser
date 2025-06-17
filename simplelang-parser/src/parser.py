class SimpleLangParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if tokens else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def match(self, expected_type=None, expected_value=None):
        if self.current_token:
            if (expected_type is None or self.current_token['type'] == expected_type) and \
               (expected_value is None or self.current_token['value'] == expected_value):
                print(f"Matched: {self.current_token}")
                self.advance()
                return True
            else:
                raise SyntaxError(
                    f"Expected {expected_type} ({expected_value}), got {self.current_token['type']} ({self.current_token['value']}) at line {self.current_token['line']}"
                )
        else:
            raise SyntaxError("Unexpected end of input")

    def parse_program(self):
        try:
            while self.current_token:
                self.parse_statement()
            print("Parsing successful.")
        except Exception as e:
            print(f"Syntax Error: {e}")

    def parse_statement(self):
        if self.current_token['type'] == 'KEYWORD' and self.current_token['value'] in ['int', 'bool', 'string']:
            self.parse_declaration()
        elif self.current_token['type'] == 'IDENTIFIER':
            self.parse_assignment()
        elif self.current_token['type'] == 'KEYWORD' and self.current_token['value'] == 'if':
            self.parse_if()
        elif self.current_token['type'] == 'KEYWORD' and self.current_token['value'] == 'for':
            self.parse_for()
        else:
            raise SyntaxError(f"Unexpected statement at line {self.current_token['line']}")

    def parse_declaration(self):
        self.match('KEYWORD')  # type
        self.match('IDENTIFIER')
        self.match('SYMBOL', ';')

    def parse_assignment(self):
        self.match('IDENTIFIER')
        self.match('OPERATOR', '=')
        self.parse_expression()
        self.match('SYMBOL', ';')

    def parse_expression(self):
        self.parse_simple_expression()
        if self.current_token and self.current_token['type'] == 'OPERATOR' and self.current_token['value'] in ['==', '!=', '<=', '>=', '<', '>']:
            self.match('OPERATOR')
            self.parse_simple_expression()

    def parse_simple_expression(self):
        self.parse_term()
        while self.current_token and self.current_token['type'] == 'OPERATOR' and self.current_token['value'] in ['+', '-']:
            self.match('OPERATOR')
            self.parse_term()

    def parse_term(self):
        self.parse_factor()
        while self.current_token and self.current_token['type'] == 'OPERATOR' and self.current_token['value'] in ['*', '/']:
            self.match('OPERATOR')
            self.parse_factor()

    def parse_factor(self):
        if self.current_token['type'] in ['IDENTIFIER', 'NUMBER', 'STRING']:
            self.match(self.current_token['type'])
        elif self.current_token['type'] == 'KEYWORD' and self.current_token['value'] in ['true', 'false']:
            self.match('KEYWORD')
        elif self.current_token['type'] == 'SYMBOL' and self.current_token['value'] == '(':
            self.match('SYMBOL', '(')
            self.parse_expression()
            self.match('SYMBOL', ')')
        else:
            raise SyntaxError(f"Invalid factor at line {self.current_token['line']}")

    def parse_condition(self):
        self.parse_expression()

    def parse_if(self):
        self.match('KEYWORD', 'if')
        self.match('SYMBOL', '(')
        self.parse_condition()
        self.match('SYMBOL', ')')
        self.match('SYMBOL', '{')
        while self.current_token and self.current_token['value'] != '}':
            self.parse_statement()
        self.match('SYMBOL', '}')

    def parse_for(self):
        self.match('KEYWORD', 'for')
        self.match('SYMBOL', '(')
        self.parse_declaration()
        self.parse_expression()
        self.match('SYMBOL', ';')
        self.parse_assignment()
        self.match('SYMBOL', ')')
        self.match('SYMBOL', '{')
        while self.current_token and self.current_token['value'] != '}':
            self.parse_statement()
        self.match('SYMBOL', '}')