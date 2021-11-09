def anti_vowel(text):
    result = ''
    vowels = 'aeiuoAEIUO'
    for char in text:
        if char not in vowels:
            result += char
    return result


print(anti_vowel("Divya gaur"))
