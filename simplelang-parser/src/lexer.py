import re


TOKEN_SPECS = [
    ("KEYWORD", r"\b(int|bool|string|if|for|while)\b"),
    ("IDENTIFIER", r"\b[a-zA-Z][a-zA-Z0-9]*\b"),
    ("NUMBER", r"\b\d+\b"),
    ("OPERATOR", r"[+\-*/=<>!&|]"),
    ("SYMBOL", r"[;(){},]"),
    ("WHITESPACE", r"\s+"),
]

def tokenize(code):
    tokens = []
    while code:
        match = None
        for token_type, regex in TOKEN_SPECS:
            match = re.match(regex, code)
            if match:
                value = match.group(0)
                if token_type != "WHITESPACE":
                    tokens.append({"type": token_type, "value": value})
                code = code[len(value):]
                break
        if not match:
            raise SyntaxError(f"Invalid character: {code[0]}")
    return tokens
