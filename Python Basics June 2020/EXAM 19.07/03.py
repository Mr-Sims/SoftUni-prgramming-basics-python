windows_count = int(input())
window_type = input()
shipping = input()
price_per_window = 0

if windows_count >= 10:
    if window_type == "90X130":
        price_per_window = 110
        if  windows_count > 60:
            price_per_window = price_per_window * 0.92
        elif 30 <= windows_count <= 60:
            price_per_window = price_per_window * 0.95
    elif window_type == "100X150":
        price_per_window = 140
        if windows_count > 80:
            price_per_window = price_per_window * 0.9
        elif 40 < windows_count <= 80 :
            price_per_window = price_per_window * 0.94
    elif window_type == "130X180":
        price_per_window = 190
        if windows_count > 50:
            price_per_window = price_per_window * 0.88
        elif 20 < windows_count <= 50:
            price_per_window = price_per_window * 0.93
    elif window_type == "200X300":
        price_per_window = 250
        if windows_count > 50:
            price_per_window = price_per_window * 0.86
        elif 25 < windows_count <= 50:
            price_per_window = price_per_window * 0.91
    if shipping == "With delivery":
        if windows_count > 99:
            total = ((price_per_window * windows_count) + 60) * 0.96
            print(f"{total:.2f} BGN")
        else:
            total = (price_per_window * windows_count) + 60
            print(f"{total:.2f} BGN")
    else:
        if windows_count > 99:
            total = (price_per_window * windows_count) * 0.96
            print(f"{total:.2f} BGN")
        else:
            total = price_per_window * windows_count
            print(f"{total:.2f} BGN")
else:
    print("Invalid order")