def convert(number: int) -> str:
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }

    output_sound = ''
    for factor, sound in sounds.items():
        if number % factor == 0:
            output_sound += sound

    return str(number) if not output_sound else output_sound
