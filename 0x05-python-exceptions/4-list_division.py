#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    divdend = 0
    result = []
    while i < list_length:
        try:
            divdend = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divdend = 0
        except ZeroDivisionError:
            print("division by 0")
            divdend = 0
        except IndexError:
            print("out of range")
            divdend = 0
        finally:
            result.append(divdend)
        i += 1
    return result
