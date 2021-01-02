n = int(input())
opened = False
closed = False
balanced = False
must_balance = False

for i in range(0, n):
    string = input()
    if string == "(":
        opened = True
        if not closed:
            must_balance = True
            balanced = False
        else:
            balanced = True
    elif string == ")":
        closed = True
        if opened:
            must_balance = False
            balanced = True
            opened = False
            closed = False
        else:
            balanced = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
