import pytest
from src.lexer import lex, Token, TokenType


@pytest.mark.parametrize(
    "payload,expected",
    [
        ("", []),
        ("  ", []),
        ("3", [Token(TokenType.NUMBER, 3)]),
        ("3.14", [Token(TokenType.NUMBER, 3.14)]),
        ("+", [Token(TokenType.PLUS, "+")]),
        ("3 + 4", [Token(TokenType.NUMBER, 3), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, 4)]),
        ("(3 + 4) * 2", [
            Token(TokenType.LPAREN, "("),
            Token(TokenType.NUMBER, 3),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.TIMES, "*"),
            Token(TokenType.NUMBER, 2)
        ])
    ],
)
def test_lexer(payload: str, expected: list[Token]):
    content = list(lex(iter(payload)))
    assert content == expected


def test_invalid_character():
    content = "2a +1"
    
    with pytest.raises(ValueError, match=r"Unexpected character after number: a"):
        list(lex(iter(content)))


def test_number_starting_with_zero():
    content = "012 + 3"

    with pytest.raises(ValueError, match=r"integer values shouldn't start with 0"):
        list(lex(iter(content)))

