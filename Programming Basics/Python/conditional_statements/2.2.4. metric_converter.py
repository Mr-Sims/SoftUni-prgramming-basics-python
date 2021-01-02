#МОЕ РЕШЕНИЕ
lenght_input = float(input())
metric_input = str(input())
metric_output = str(input())
if metric_input == "mm" and metric_output == "m":
    print(f" {(lenght_input / 1000):.3f}")
elif metric_input == "mm" and metric_output == "cm":
    print(f" {(lenght_input / 10):.3f}")
elif metric_input == "m" and metric_output == "cm":
    print(f" {(lenght_input * 100):.3f}")
elif metric_input == "m" and metric_output == "mm":
    print(f" {(lenght_input * 1000):.3f}")
elif metric_input == "cm" and metric_output == "mm":
    print(f" {(lenght_input * 10):.3f}")
elif metric_input == "cm" and metric_output == "m":
    print(f" {(lenght_input / 100):.3f}")






# num = float(input())
# input_metric = input()
# output_metric = input()
#
# if input_metric == "mm":
#     num /= 1000
# elif input_metric == "cm":
#     num /= 100
# if output_metric == "mm":
#     num *= 1000
# elif output_metric == "cm":
#     num *= 100
# print(f"{num:.3f}")
