import queue
from lexer import Token, TokenType, lex

class ShuntingYard:
    def __init__(self, tokens: list, q: queue.Queue, stack: list):
        self.tokens = tokens
        self.q = q
        self.stack = stack


