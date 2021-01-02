# таксата за участие на велосипедистите. Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%. Организаторите отделят 5% процента от събраната сума за разходи.
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.

junior_count = int(input()) #броят младши велосипедисти. Цяло число
senior_count = int(input()) # старши велосипедисти. Цяло число
track_type = input() # вид трасе – "trail", "cross-country", "downhill" или "road"
sum = 0

if track_type == "trail":
    sum = ((junior_count * 5.5) + (senior_count * 7)) * 0.95
elif track_type == "cross-country":
    sum = ((junior_count * 8) + (senior_count * 9.5)) * 0.95
    if junior_count + senior_count >= 50:
        sum = ((junior_count * (8 * 0.75)) + (senior_count * (9.5 * 0.75))) * 0.95
elif track_type == "downhill":
    sum = ((junior_count * 12.25) + (senior_count * 13.75)) * 0.95
elif track_type == "road":
    sum = ((junior_count * 20) + (senior_count * 21.5)) * 0.95
print(f"{sum:.2f}")
