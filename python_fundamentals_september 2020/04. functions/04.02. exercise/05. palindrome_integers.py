int_str = input()

int_lst = int_str.split(", ")


def palindrome_check(a):
    for el in int_lst:
        rev = ""
        for i in reversed(el):
            rev += i
        if el == rev:
            print("True")
        else:
            print("False")


palindrome_check(int_lst)