company_database = {}

while True:
    line = input().split(" -> ")
    if line[0] == "End":
        break

    company = line[0]
    employee_id = line[1]

    if company not in company_database:
        company_database[company] = []
        company_database[company].append(employee_id)

    elif company in company_database:
        if employee_id in company_database[company]:
            continue
        elif employee_id not in company_database[company]:
            company_database[company].append(employee_id)


sort_by_company = dict(sorted(company_database.items(), key=lambda x: x[0]))
for key, value in sort_by_company.items():
    print(f"{key}")
    for val in value:
        print(f"-- {val}")
