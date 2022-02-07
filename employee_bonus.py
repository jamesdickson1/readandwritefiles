
import csv

infile = open("EmployeePay.csv", "r")

bonusfile = csv.reader(infile, delimiter=",")

next(bonusfile)

for record in bonusfile:
    
    bonus = float(record[3]) * float(record[4])
    total = float(record[3]) * bonus
    formatbonus = "{:.2f}".format(bonus)

    print("FName: " + record[1])
    print("LName: " + record[2])
    print("Salary: $" + record[3])
    print("Bonus: $" + str(formatbonus))
    print("Total Pay: $" + str(float(record[3]) + bonus))

    input()


infile.close

