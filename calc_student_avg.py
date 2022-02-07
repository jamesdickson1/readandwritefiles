
import csv

infile = open("Student_Scores.csv",'r')

outfile = open("Student_avg.csv",'w')

scores = csv.reader(infile,delimiter=",")


for record in scores:
    avg = ((float(record[1]) + float(record[2]) + float(record[3]))/3)
    formatavg = "{:.2f}".format(avg)
    outfile.write(record[0] + " " + str(formatavg) + "\n")
    print (avg)

outfile.close
