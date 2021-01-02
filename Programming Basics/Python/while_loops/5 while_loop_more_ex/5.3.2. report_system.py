# На благотворително събитие плащанията за закупените продукти винаги се редуват:
# плащане в брой и плащане с карта.
# Установени са следните правила за заплащане:
# •	Ако продуктът надвишава 100лв., за него не може да се плати в брой
# •	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.

goal_sum = int(input())
credit_card = 0
cash = 0
count = 0
credit_card_count = 0
cash_count = 0
total_sum = 0

line = input()
while line != "End":
    product_price = int(line)
    count += 1
    if count % 2 != 0:
        if product_price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_sum += product_price
            cash += product_price
            cash_count += 1
    else:
        if product_price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_sum += product_price
            credit_card += product_price
            credit_card_count += 1
    if total_sum >= goal_sum:
        avg_cash = cash / credit_card_count
        avg_credit = credit_card / credit_card_count
        print(f"Average CS: {avg_cash:.2f}")
        print(f"Average CC: {avg_credit:.2f}")
        break
    line = input()
if total_sum < goal_sum:
    print("Failed to collect required money for charity.")

# Изход
# На конзолата да се отпечата:
# •	При успешна транзакция: "Product sold!"
# •	При неуспешна транзакция: "Error in transaction!"
# •	Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да приключи и на конзолата да се изпишат два реда:
# o	"Average CS: {средно плащане в кеш на човек}"
# o	"Average CC: {средно плащане с карта на човек}"
#               Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
# •	При получаване на команда "End", да се изпише един ред:
# o	"Failed to collect required money for charity."

