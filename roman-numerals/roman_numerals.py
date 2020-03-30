_symbols_map = {
    1: ['I', 'V', 'X'],
    2: ['X', 'L', 'C'],
    3: ['C', 'D', 'M'],
    4: ['M']
}


def roman(number: int):
    digits = str(number)
    digits_length = len(digits)

    return ''.join([_get_roman_digit(int(digit), digits_length - i) for i, digit in enumerate(digits)])


def _get_roman_digit(number: int, position: int) -> str:
    subset = _symbols_map[position]

    if number == 0:
        return ''
    if number <= 3:
        return subset[0] * number
    elif number == 4:
        return subset[0] + subset[1]
    elif number == 5:
        return subset[1]
    elif number < 9:
        return subset[1] + subset[0]*(number-5)
    else:
        return subset[0] + subset[2]

