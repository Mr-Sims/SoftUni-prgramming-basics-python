page_count = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_day = ( page_count / days ) / pages_per_hour

print(hours_per_day)