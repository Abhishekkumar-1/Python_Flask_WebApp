def search4vowels(phrase: str)->set:
    '''Returns the set of vowel found in 'phrase'.'''
    return set('aeiou').intersection(set(phrase))

def search4letters(phrase:str,letters: str='aeiou')->set:
    '''returns the set of 'letters' found in phrase.'''
    return set(letters).intersection(set(phrase))
