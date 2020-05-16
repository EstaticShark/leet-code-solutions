
def romanToInt(s: str) -> int:
    roman_keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    str_length = s.__len__()
    i = 0
    number = 0

    while i < str_length - 1:
        if roman_keys[s[i]] < roman_keys[s[i + 1]]:
            number += (roman_keys[s[i+1]] - roman_keys[s[i]])
            i += 2
        else:
            number += roman_keys[s[i]]
            i += 1

    if i < str_length:
        number += roman_keys[s[i]]

    print(number)
#MCMXCIV
if __name__ == "__main__":
    str_input = input("Enter number in roman")
    romanToInt(str_input)