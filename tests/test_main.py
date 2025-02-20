import pytest
import queue
from src.lexer import Token, TokenType
from src.main import shunting_yard_algorithm

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
                Token(TokenType.NUMBER, "2")
            ],
            [
                Token(TokenType.NUMBER, "3"),
                Token(TokenType.NUMBER, "4"),
                Token(TokenType.PLUS, "+"),
                Token(TokenType.NUMBER, "2"),
                Token(TokenType.TIMES, "*")
            ]
        ),
    ]
)
def test_shunting_yard_algorithm(tokens, expected):
    content = shunting_yard_algorithm(tokens, q=queue.Queue(), stack=[])
    assert content == expected


 