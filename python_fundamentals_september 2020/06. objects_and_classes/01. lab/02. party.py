# ############## Решение Йордан Джамбазов ##################################
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Party:
#     def __init__(self):
#         self.people = []
#
#     def invite(self, person):
#         self.people.append(person)
#
#     def names_of_atendees(self):
#         return ", ".join([person.name for person in self.people])
#
#     def number_of_atendees(self):
#         return len(self.people)
#
# party = Party()
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     name = command
#     person = Person(name)
#     party.invite(person)
#
# print(f"Going: {party.names_of_atendees()}")
# print(f"Total: {party.number_of_atendees()}")
#

########################################################################
################################## Решение Добри Стоилов ################################


class Party:
    def __init__(self):
        self.people = []


    def go(self, name):
        self.people.append(name)


    def get_going(self):
        return f'Going: {", ".join(self.people)}'


    def get_count(self):
        return f'Total: {len(self.people)}'


party = Party()

while True:

    name = input()
    if name == "End":
        break
    party.go(name)

print(party.get_going())
print(party.get_count())