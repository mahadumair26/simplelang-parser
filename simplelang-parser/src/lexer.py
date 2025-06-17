import re

TOKEN_SPECS = [
    ("KEYWORD", r"\b(int|bool|string|if|for|while|true|false)\b"),
    ("STRING", r'"[^"]*"'),
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ("NUMBER", r'\b\d+\b'),
    ("OPERATOR", r'(==|!=|<=|>=|&&|\|\||[+\-*/=<>])'),
    ("SYMBOL", r'[;(){}:,]'),
    ("WHITESPACE", r'\s+'),
]

def tokenize(code):
    tokens = []
    line_number = 1
    while code:
        match = None
        for token_type, regex in TOKEN_SPECS:
            pattern = re.compile(regex)
            match = pattern.match(code)
            if match:
                value = match.group(0)
                if token_type != "WHITESPACE":
                    tokens.append({"type": token_type, "value": value, "line": line_number})
                code = code[len(value):]
                # Count newlines in matched text to update line number
                line_count = value.count('\n')
                line_number += line_count
                break
        if not match:
            raise SyntaxError(f"Invalid character at line {line_number}: '{code[0]}'")
    return tokens