days_count = int(input())
total_food_supply = float(input())
total_dog = 0
total_cat = 0
total_biscuits = 0.5

for i in range (1, days_count + 1):

    dog_ate = int(input())
    total_dog += dog_ate
    cat_ate = int(input())
    total_cat += cat_ate

    if i % 3 == 0:
        total_biscuits += (dog_ate + cat_ate) * 0.1
percentage_both = ((total_cat + total_dog) / total_food_supply) * 100
percentage_dog = (total_dog / (total_cat+total_dog)) * 100
percentage_cat = (total_cat / (total_cat + total_dog)) * 100


print(f"Total eaten biscuits: {int(total_biscuits)}gr.")
print(f"{percentage_both:.2f}% of the food has been eaten.")
print(f"{percentage_dog:.2f}% eaten from the dog.")
print(f"{percentage_cat:.2f}% eaten from the cat.")