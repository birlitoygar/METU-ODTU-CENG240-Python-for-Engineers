given_debt = float(input())
total_cash = given_debt * (1.02**6)
pay_for_month = total_cash / 6

print("{:.2f}".format(pay_for_month))