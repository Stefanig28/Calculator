import pytest
from src.lexer import Token, TokenType
from src.main import shunting_yard_algorithm, main


@pytest.mark.parametrize(
    "tokens, expected",
    [
        ([], []),
        (
            [
                Token(TokenType.LPAREN, "("),
                Token(TokenType.NUMBER, "3"),
                Token(TokenType.PLUS, "+"),
                Token(TokenType.NUMBER, "4"),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.TIMES, "*"),
                Token(TokenType.NUMBER, "2"),
            ],
            [
                Token(TokenType.NUMBER, "3"),
                Token(TokenType.NUMBER, "4"),
                Token(TokenType.PLUS, "+"),
                Token(TokenType.NUMBER, "2"),
                Token(TokenType.TIMES, "*"),
            ],
        ),
    ],
)
def test_shunting_yard_algorithm(tokens, expected):
    content = shunting_yard_algorithm(tokens)
    assert content == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (
            [
                Token(TokenType.NUMBER, 1),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.PLUS, "+"),
            ],
            3,
        ),
        (
            [
                Token(TokenType.NUMBER, 5),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.MINUS, "-"),
            ],
            3,
        ),
        (
            [
                Token(TokenType.NUMBER, 3),
                Token(TokenType.NUMBER, 4),
                Token(TokenType.TIMES, "*"),
            ],
            12,
        ),
        (
            [
                Token(TokenType.NUMBER, 8),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.DIVIDE, "/"),
            ],
            4,
        ),
        (
            [
                Token(TokenType.NUMBER, 3.5),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.TIMES, "*"),
            ],
            7.0,
        ),
        (
            [
                Token(TokenType.NUMBER, 10),
                Token(TokenType.NUMBER, 5),
                Token(TokenType.DIVIDE, "/"),
                Token(TokenType.NUMBER, 2),
                Token(TokenType.TIMES, "*"),
            ],
            4,
        ),
    ],
)
def test_main(tokens, expected):
    assert main(tokens) == expected
