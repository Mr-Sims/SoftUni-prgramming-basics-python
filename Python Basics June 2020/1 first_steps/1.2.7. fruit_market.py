#Input data
strawberry_prc = float(input()) #57.5
bananas_qnt = float(input()) #10
oranges_qnt = float(input()) # 3.4
raspberry_qnt = float(input()) # 6.5
strawberry_qnt = float(input()) # 1.7
#problem logic
raspberry_prc = strawberry_prc * 0.5
oranges_prc = raspberry_prc - (raspberry_prc * 0.4)
bananas_prc = raspberry_prc - (raspberry_prc * 0.8)
total_sum = raspberry_qnt * raspberry_prc + oranges_qnt * oranges_prc + bananas_qnt * bananas_prc + strawberry_qnt * strawberry_prc
#print the output
print(total_sum)