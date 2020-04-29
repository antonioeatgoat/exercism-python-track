def two_fer(name: str = '') -> str:
    if not name:
        name = 'you'

    return f'One for {name}, one for me.'
