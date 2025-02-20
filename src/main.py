import queue
from src.lexer import Token, TokenType, lex


def shunting_yard_algorithm(tokens: list[Token]) -> list[queue.Queue]:
    q = queue.Queue()
    stack = []

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
                raise ValueError(
                    "Mismatched parentheses: no opening parenthesis found."
                )
        else:
            while stack and stack[-1].type.precedence >= token.type.precedence:
                q.put(stack.pop())
            stack.append(token)

    while stack:
        q.put(stack.pop())

    return list(q.queue)


def main(tokens: list[queue.Queue]) -> int:
    stack = []

    for token in tokens:
        if token.type == TokenType.NUMBER:
            stack.append(token.value)
        else:
            second = stack.pop()
            first = stack.pop()

            if token.value == "+":
                result = first + second
            elif token.value == "-":
                result = first - second
            elif token.value == "*":
                result = first * second
            elif token.value == "/":
                result = first / second

            stack.append(result)

    return stack[0]


def _cli() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("-calc", dest="calculator", type=str)
    args = parser.parse_args()

    tokens = lex(iter(args.calculator))
    result = main(shunting_yard_algorithm(tokens))

    print(result)
    sys.exit(0)


if __name__ == "__main__":
    _cli()
