from lexer import tokenize
from error import SyntaxError

class SimpleLangParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def match(self, token_type):
        if self.current_token and self.current_token['type'] == token_type:
            self.next_token()
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def parse_program(self):
        self.parse_declaration_list()
        self.parse_statement_list()

    def parse_declaration_list(self):
        while self.current_token and self.current_token['type'] in ['KEYWORD']:
            self.parse_declaration()

    def parse_declaration(self):
        self.match("KEYWORD")
        self.match("IDENTIFIER")
        self.match("SYMBOL")  # Match the semicolon

    def parse_statement_list(self):
        while self.current_token:
            self.parse_statement()

    def parse_statement(self):
        if self.current_token['type'] == 'KEYWORD' and self.current_token['value'] == 'if':
            self.parse_if_statement()
        elif self.current_token['type'] == 'KEYWORD' and self.current_token['value'] == 'for':
            self.parse_for_statement()
        else:
            self.parse_assignment()

    def parse_if_statement(self):
        self.match('KEYWORD')  # Match 'if'
        self.match('SYMBOL')   # Match '('
        self.parse_expression()
        self.match('SYMBOL')   # Match ')'
        self.match('SYMBOL')   # Match '{'
        self.parse_statement_list()
        self.match('SYMBOL')   # Match '}'

    def parse_assignment(self):
        self.match('IDENTIFIER')
        self.match('OPERATOR')
        self.parse_expression()
        self.match('SYMBOL')  # Match semicolon

    def parse_expression(self):
        self.match('NUMBER')
        # Implement more rules for expressions

if __name__ == "__main__":
    code = "int x; x = 10;"
    tokens = tokenize(code)
    parser = SimpleLangParser(tokens)
    parser.parse_program()
