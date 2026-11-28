# calculate total and net salary where variable are bassic salary , bonus,hra and pf is 7.8% on basic salary.

basic_salary = float(input("Enter Basic Salary: "))
bonus = float(input("Enter Bonus: "))
hra = 0.2 * basic_salary
pf = 0.078 * basic_salary
total_salary = basic_salary + bonus + hra
net_salary = total_salary - pf
print("Total Salary =", total_salary)
print("Net Salary =", net_salary)
