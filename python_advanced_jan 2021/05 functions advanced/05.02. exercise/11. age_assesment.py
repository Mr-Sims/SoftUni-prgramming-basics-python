def age_assignment(*names, **kwargs):
    new_dict = {}
    for name in names:
        new_dict[name] = kwargs[name[0]]
    return new_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))