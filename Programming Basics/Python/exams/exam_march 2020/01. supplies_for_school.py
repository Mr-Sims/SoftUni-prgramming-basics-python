pens = 5.8
markers = 7.2
cleaning_thingy = 1.2
pens_count = int(input())
markers_count = int(input())
clean_count = float(input())
rebaja = int(input())

total = pens * pens_count + markers * markers_count + cleaning_thingy * clean_count
end_sum = total - ((total * rebaja) / 100)
print(f"{end_sum:.3f}")