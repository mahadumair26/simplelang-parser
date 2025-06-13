from lexer import tokenize
from parser import SimpleLangParser

def run_parser(source_code):
    # Tokenize the input SimpleLang source code
    tokens = tokenize(source_code)
    # Create a parser instance with the tokens
    parser = SimpleLangParser(tokens)
    # Run the parsing logic
    parser.parse_program()

if __name__ == "__main__":
    # Define a simple test case (you can update it with your source code)
    code = """
    int x
    x = 10;
    """
    
    try:
        run_parser(code)
        print("Parsing completed successfully")
    except Exception as e:
        print(f"Error during parsing: {e}")
