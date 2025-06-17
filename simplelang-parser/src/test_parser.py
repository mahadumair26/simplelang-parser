from lexer import tokenize
from parser import SimpleLangParser

def run_parser(source_code):
    tokens = tokenize(source_code)
    parser = SimpleLangParser(tokens)
    parser.parse_program()

def test_valid_program():
    valid_code = """
    int x;
    bool flag;
    string name;

    x = 10;
    flag = true;
    name = "SimpleLang";

    if (x > 0) {
        x = x - 1;
    }

    for (int i = 0; i < 10; i = i + 1) {
        name = "Loop";
    }
    """
    print("=== Test Case 1: Valid Program ===")
    run_parser(valid_code)

def test_invalid_declaration():
    invalid_declaration_code = """
    int x
    x = 10;
    """
    print("=== Test Case 2: Invalid Declaration ===")
    run_parser(invalid_declaration_code)

def test_missing_curly_brace():
    missing_brace_code = """
    int x;
    x = 10;

    if (x > 0) {
        x = x - 1;
    """
    print("=== Test Case 3: Missing Curly Brace ===")
    run_parser(missing_brace_code)

def test_invalid_assignment():
    invalid_assignment_code = """
    int x;
    x = true;
    """
    print("=== Test Case 4: Invalid Assignment ===")
    run_parser(invalid_assignment_code)

def test_invalid_control_structure():
    invalid_control_structure_code = """
    int x;
    x = 10;

    if x > 0 {
        x = x - 1;
    }
    """
    print("=== Test Case 5: Invalid Control Structure ===")
    run_parser(invalid_control_structure_code)

if __name__ == "__main__":
    test_valid_program()
    test_invalid_declaration()
    test_missing_curly_brace()
    test_invalid_assignment()
    test_invalid_control_structure()