def score(word):
    return sum([_get_points_by_letter(x) for x in word])


def _get_points_by_letter(letter: str) -> int:
    for points, letters in _points_table().items():
        if letter.upper() in letters:
            return points

    return 0


def _points_table() -> []:
    return {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ',
    }
