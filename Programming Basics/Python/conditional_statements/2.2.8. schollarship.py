from math import floor
income = float(input())
average_score = float(input())
basic_income = float(input())
results_scholarship_coef = 25
social_scholarship = basic_income * 0.35
results_scholarship = average_score * results_scholarship_coef

if basic_income > income and average_score >= 5.5:
    if results_scholarship >= social_scholarship:
        print(f"You get a scholarship for excellent results {floor(results_scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif basic_income > income and average_score > 4.50:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif average_score >= 5.5:
    print(f"You get a scholarship for excellent results {floor(results_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")
