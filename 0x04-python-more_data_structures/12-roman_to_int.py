#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None
    equ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    leng = len(roman_string)
    num = 0
    for i in range(leng):
        if i != leng - 1 and equ[roman_string[i]] < equ[roman_string[i + 1]]:
            num -= equ[roman_string[i]]
        else:
            num += equ[roman_string[i]]
    return num

# num = 0
# roman_num = ["I", "V", "X", "L", "C", "D", "M"]
# leng = len(roman_string)
# for i in range(leng):
#     if roman_string[i] == "I":
#         if i != leng - 1 and roman_string[i + 1] in roman_num[1:]:
#             num -= 1
#             continue
#         num += 1
#     if roman_string[i] == "V":
#         if i != leng - 1 and roman_string[i + 1] in roman_num[2:]:
#             num -= 5
#             continue
#         num += 5
#     if roman_string[i] == "X":
#         if i != leng - 1 and roman_string[i + 1] in roman_num[3:]:
#             num -= 10
#             continue
#         num += 10
#     elif roman_string[i] == "L":
#         if i != leng - 1 and roman_string[i + 1] in roman_num[4:]:
#             num -= 50
#             continue
#         num += 50
#     elif roman_string[i] == "C":
#         if i != leng - 1 and roman_string[i + 1] in roman_num[5:]:
#             num -= 100
#             continue
#         num += 100
#     elif roman_string[i] == "D":
#         if i != leng - 1 and roman_string[i + 1] in roman_num[6:]:
#             num -= 500
#             continue
#         num += 500
#     elif roman_string[i] == "M":
#         num += 1000
# return num
