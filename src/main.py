import queue
from . import lexer, shunting_yard


def main(calculate: str) -> int:
    tokens = [char for char in calculate if char != ' ']
    q = queue.Queue()
    stack = []

    while tokens:
        for token in tokens:
            return tokens





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

