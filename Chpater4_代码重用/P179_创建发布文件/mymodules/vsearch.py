def search4Vowels(phrase: str) -> set:
    """Return a set of the vowels found in phrase"""
    vowels = set('aeiou')
    return set(vowels).intersection(set(phrase))


def search4Letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in phrase"""
    return set(letters).intersection(set(phrase))
