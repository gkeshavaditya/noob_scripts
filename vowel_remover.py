def anti_vowel(text):
    result = ''
    vowels = 'aeiuoAEIUO'
    for char in text:
        if char not in vowels:
            result += char
    print result
    return result

anti_vowel('I hate when I dont program good')