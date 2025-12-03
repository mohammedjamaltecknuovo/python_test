with open("carSale.csv") as f:
    lines = f.readlines()

companies = []
sales = []

for x in range(0, len(lines), 2):
    company_line = lines[x].strip()
    numbers_line = lines[x + 1].strip()
    companies.append(company_line)
    parts = numbers_line.split(",")
    numbers = list(map(int, parts))
    sales.append(numbers)

monthly_totals = []

for month_index in range(8):
    total = 0
    for company_sales in sales:
        total += company_sales[month_index]
    monthly_totals.append(total)

yearly_totals = []

for company_sales in sales:
    yearly_totals.append(sum(company_sales))

grand_total = sum(yearly_totals)

for total in monthly_totals:
    print(total)

print("Grand total:", grand_total)
