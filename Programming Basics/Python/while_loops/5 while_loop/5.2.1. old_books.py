# Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга или не провери всички в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст).
# Книгите в библиотеката са свършили щом получите текст “No More Books”.
# Ако не открие търсената книгата, да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си, да се отпечата на един ред:
# o	"You checked {брой} books and found it."
book = input()
book_count = 0
current_book = input()
while current_book != "No More Books":
    if current_book == book:
        print(f"You checked {book_count} books and found it.")
        break
    book_count += 1
    current_book = input()
if current_book == "No More Books":
    print(f"The book you search is not here!\nYou checked {book_count} books.")