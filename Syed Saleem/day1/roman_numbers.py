def int_to_roman(num):
    if   not 1 <= num <= 3999:
        return "Number out of range (1-3999)"

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for value, symbol in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while num >= value:
            result += symbol
            num -= value

    return result

# Example usage:
number = int(input("enter the number you waNT TO CONVERTY TO ROMANS : "))
roman_numeral = int_to_roman(number)
print(f"{number} in Roman numerals is: {roman_numeral}")
    