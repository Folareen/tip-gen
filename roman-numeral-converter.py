def convertToRoman(num):
    ROMAN_NUMERALS = {
        "M" :1000,
        "CM":	900,
        "D"	:500,
        "CD":	400,
        "C"	:100,
        "XC":	90,
        "L"	:50,
        "XL":	40,
        "X"	:10,
        "IX":	9,
        "V"	:5,
        "IV":	4,
        "I"	:1
    }
    romanNumeral = ""

    for roman in ROMAN_NUMERALS :
        number = ROMAN_NUMERALS[roman]
    
        while(num >= number):
            num -= number
            romanNumeral += roman

    return romanNumeral

print(convertToRoman(36))