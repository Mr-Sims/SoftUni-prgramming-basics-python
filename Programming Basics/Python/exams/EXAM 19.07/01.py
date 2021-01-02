company_name = input()
adult_tickets_count = int(input())
child_ticket_count = int(input())
net_adult_ticket_cost = float(input())
service_tax = float(input())

net_child_ticket_cost = net_adult_ticket_cost * 0.3
final_adult_ticket_price = net_adult_ticket_cost + service_tax
final_child_ticket_price = net_child_ticket_cost + service_tax
sum_adult_tickets = final_adult_ticket_price * adult_tickets_count
sum_child_tickets = final_child_ticket_price * child_ticket_count
total_sum = sum_adult_tickets + sum_child_tickets
net_profit = total_sum * 0.2

print(f"The profit of your agency from {company_name} tickets is {net_profit:.2f} lv.")