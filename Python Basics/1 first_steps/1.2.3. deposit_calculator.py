deposited_sum = float(input())
deposit_term = float(input())
interest_rate = (float(input()) / 100)

end_deposit_sum = deposited_sum + deposit_term * ((deposited_sum * interest_rate) / 12)

print(end_deposit_sum)