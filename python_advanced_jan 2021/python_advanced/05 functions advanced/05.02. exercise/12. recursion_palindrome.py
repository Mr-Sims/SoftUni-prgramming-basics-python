#########################################################################
#########################################################################
### working 100/100

def palindrome(word, index):
    middle = int(len(word) / 2)
    if middle == index:
        return f"{word} is a palindrome"
    if word[index] == word[::-1][index]:

        return palindrome(word, index + 1)
    else:
        return f"{word} is not a palindrome"


#########################################################################
#########################################################################
## working 33/100


def palindrome(word, index):
    is_palindrome = False
    if len(word) == 0:
        return
    if word[0] == word[::-1][0]:
        palindrome(word[1:-1], index+1)
        is_palindrome = True
        if is_palindrome:
            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"
    else:
        return f"{word} is not a palindrome"


##########################################################################
##########################################################################
### working 33/100


def palindrome(word, index=0, end_index=-1):
    if index == len(word):
        return f"{word} is a palindrome"
    if word[index] == word[end_index]:
        palindrome(word, index + 1, end_index - 1)

    else:
        return f"{word} is not a palindrome"

##############################################################################
##############################################################################
#######################  HELP FROM A FRIEND SOLUTIONS ########################


def palindrome1(word, index):
    middel = int(len(word) / 2)
    if middel == index:
        return f"{word} is a palindrome"
    if word[index] != word[::-1][index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


##############################################################################
##############################################################################
#######################  HELP FROM A FRIEND SOLUTIONS ########################


def palindrome_almost_coorect(word, index):
    if len(word) == 0 or len(word) == 1:
        return f"{word} is a palindrome"
    if word[index] != word[::-1][index]:
        return f"{word} is not a palindrome"
    return palindrome(word[1:-1], index)


##############################################################################
##############################################################################
#######################  HELP FROM A FRIEND SOLUTIONS ########################


def palindrome(word, index):
    def rec(word):
        if len(word) == 0 or len(word) == 1:
            return True
        if word[0] != word[::-1][0]:
            return False
        return rec(word[1:-1])

    if rec(word):
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome("aabpeterbaa", 0))
