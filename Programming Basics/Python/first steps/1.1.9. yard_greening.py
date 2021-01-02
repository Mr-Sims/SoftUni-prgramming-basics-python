# Read the data
m2 = float(input())
price_m2 = 7.61
price_disc = 0.18

#Program logic
full_pr = m2 * price_m2
disc = price_disc*full_pr
final_pr = full_pr-disc

#Print the output
print(f"The final price is: {final_pr} lv.")
print(f"The discount is: {disc} lv.")