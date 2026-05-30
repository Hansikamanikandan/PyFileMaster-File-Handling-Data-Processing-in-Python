import csv

def calculate_salary(basic_pay):
    hra = 0.20 * basic_pay
    da = 0.10 * basic_pay
    return basic_pay + hra + da

filename = input("Enter CSV file name: ")

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        emp_id = row[0]
        name = row[1]
        basic_pay = float(row[2])

        total_salary = calculate_salary(basic_pay)

        print("Employee ID:", emp_id)
        print("Name:", name)
        print("Total Salary:", total_salary)
        print()
