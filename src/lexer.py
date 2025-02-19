from collections.abc import Iterator
import enum

class TokenType(enum.Enum):
    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"

class Token:
    def __init__(self, type: TokenType, value: str):
        self.type = type
        self.value = value

def lex(payload: Iterator[str]) -> Iterator[Token]:

    for idx, c in enumerate(payload):
        if c == "+":
            yield Token(TokenType.PLUS, c)
        elif c == "-":
            yield Token(TokenType.MINUS, c) 
        elif c == "*":
            yield Token(TokenType.TIMES, c)
        elif c == "/":
            yield Token(TokenType.DIVIDE, c)
        elif c == "(":
            yield Token(TokenType.LPAREN, c)
        elif c == ")":
            yield Token(TokenType.RPAREN, c)
        elif c in _SPACES:
            continue
        elif c in _NUMERIC_CHARACTERS or c == "-":
            number, next_char = _lex_numeric(payload, c)
            yield Token(TokenType.NUMBER, number)
            yield from _handle_followup_characters(next_char)
        else:
            raise ValueError(_ERROR_MSG.format(character=c, index=idx))
        
        
def _handle_followup_characters(next_char: str) -> Iterator[Token]:

    if next_char == "+":
        yield Token(TokenType.PLUS, next_char)
    elif next_char == "-":
        yield Token(TokenType.MINUS, next_char)
    elif next_char == "*":
        yield Token(TokenType.TIMES, next_char)
    elif next_char == "/":
        yield Token(TokenType.DIVIDE, next_char)
    elif next_char == "(":
        yield Token(TokenType.LPAREN, next_char)
    elif next_char == ")":
        yield Token(TokenType.RPAREN, next_char)
    elif next_char in _SPACES:
        return
    else:
        raise ValueError(f"Unexpected character after number: {next_char}")

def _lex_numeric(payload: Iterator[str], c: str) -> tuple[float | int, str]:
    number = c
    for c in payload:
        if c not in _NUMERIC_CHARACTERS:
            break
        number += c

    if c == ".":
        number += c
        for c in payload:
            if c not in _NUMERIC_CHARACTERS:
                break
            number += c
        return float(number), c

    if number.startswith("0") and len(number) > 1:
        raise ValueError("integer values shouldn't start with 0")
    return int(number), c


_NUMERIC_CHARACTERS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
_SPACES = {" ", "\t", "\n"}
_ERROR_MSG = "Character {character} at index {index} is not valid"