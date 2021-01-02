user = input()
passw = input()
conf_pass = input()
while passw != conf_pass:
    conf_pass = input()
print(f"Welcome {user}!")
