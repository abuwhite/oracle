from bot.config import get_token_env


def test_get_token_env():
    actual = get_token_env()
    assert actual