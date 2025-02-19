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
    tokens = list(lex(iter(payload)))
    assert tokens == expected
