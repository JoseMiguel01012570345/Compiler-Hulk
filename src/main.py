from lexer.lexer import Lexer
from parsers.lr1_parser import LR1Parser
from cmp.languages import HulkLang
from cmp.hulk_grammar import Hulk_G
from cmp.evaluation import evaluate_reverse_parse
from semantic.semantic_chequer import Semantic_Check
import os

def main():
    lexer = Lexer(HulkLang.lexer_table(), "eof")
    parser = LR1Parser(Hulk_G)
    current_path = os.path.dirname(os.path.abspath(__file__))    
    with open(f"{current_path}/tests/test_interpreter.hulk", "r") as file:
        text = file.read()

    try:
        tokens = lexer(text)
        parse, operations = parser(tokens)
        ast = evaluate_reverse_parse(parse, operations, tokens)
        semantic = Semantic_Check()
        errors = semantic.semantic_checking(ast)
        if errors: print(errors)
        else:
            semantic.interpreter(ast)
    except SyntaxError as error:
        print(error)

    


if __name__ == "__main__":
    main()
