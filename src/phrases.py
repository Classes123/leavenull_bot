def user_left(mention: str) -> str:
    return f'{mention} покинул(а) чат.'


def user_left_with_custom_title(mention: str, custom_title: str) -> str:
    return f'{mention} ({custom_title}) покинул(а) чат.'
