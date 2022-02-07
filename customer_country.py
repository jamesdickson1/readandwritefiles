import csv

infile = open("customers.csv", "r")

outfile = open("customer_country.csv", "w")

countryfile = csv.reader(infile, delimiter=",")

counter = 0

for record in countryfile:
    outfile.write(record[1] + " " + record[2] + " , " + record[4] + "\n")
    counter += 1

print("There are " + str(counter) + " customers.")

outfile.close()
