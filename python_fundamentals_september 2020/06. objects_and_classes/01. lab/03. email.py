####################### Решение lab ######################################################

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    line = input()
    if line == "Stop":
        break

    tokens = line.split()
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())

################################### Решение Дончо ################################################


# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# class EmailManager:
#     def __init__(self):
#         self.emails = []
#
#     def add(self, email):
#         self.emails.append(email)
#
#     def send(self, index):
#         self.emails[index].send()
#
#     def print(self):
#         for email in self.emails:
#             print(email.get_info())
#
# emailManager = EmailManager()
#
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#
#     [sender, receiver, content] = command.split()
#     emailManager.add(Email(sender, receiver, content))
#
# indices_of_mails_to_send = [int(el) for el in input().split(", ")]
#
# for index in indices_of_mails_to_send:
#     emailManager.send(index)
#
# emailManager.print()