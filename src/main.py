import queue
from src.lexer import Token, TokenType


def shunting_yard_algorithm(tokens: list[Token], q: queue.Queue, stack: list) -> list[queue.Queue]:

    for token in tokens:
        if token.type == TokenType.NUMBER:
            q.put(token)
        elif token.type == TokenType.LPAREN:
            stack.append(token)
        elif token.type == TokenType.RPAREN:
            while stack and stack[-1].type != TokenType.LPAREN:
                q.put(stack.pop())
            if stack:
                stack.pop()
            else:
                raise ValueError("Mismatched parentheses: no opening parenthesis found.")
        else:
            while stack and stack[-1].type.precedence >= token.type.precedence:
                q.put(stack.pop())
            stack.append(token)

    while stack:
        q.put(stack.pop())

    return list(q.queue) 

def main(tokens: list[queue.Queue]):
    stack = []

    for token in tokens:
        

def _cli() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("-calc", dest="calculator", type=str)
    args = parser.parse_args()
    code = main(args.calculator)
    sys.exit(code)

if __name__ == "__main__":
    _cli()

