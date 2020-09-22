#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            pos = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            pos = 0
            continue
        except ZeroDivisionError:
            print("Division by 0")
            pos = 0
            continue
        except IndexError:
            print("out of range")
            pos = 0
            continue
        finally:
            res.append(pos)
    return res
