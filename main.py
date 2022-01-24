# Author: Saarim Tashfeen
# Assignment 1 CST833_350
# June 4th 2021

import csv



class Covid:


    def __init__(self, pruid, prname, prnamefr, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
        """Constructor instantiates covid object."""    # docstring
        self.pruid = pruid
        self.prname = prname
        self.prnamefr = prnamefr
        self.date = date
        self.numconf = numconf
        self.numprob = numprob
        self.numdeaths = numdeaths
        self.numtotal = numtotal
        self.numtoday = numtoday
        self.ratetotal = ratetotal

    def __str__(self):
        """Returns string of object"""
        return str(self.__dict__)


counter = 0  # counter for the loop when reading file
list = []

try:
    with open('covid19-download.csv') as csv_file: # Saarim Tashfeen
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skips the first line of file, (column names)

        for row in csv_reader: # Saarim Tashfeen
            list.append(Covid(row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[13], row[15]))
            # row[0], row[1] etc... reading columns we are only insterested in A,B,C,D,F etc...
            counter += 1
            if counter == 10:  # after 10 lines, break fom loop
                break
    for Covid in list:
        print(Covid)

    print("Saarim Tashfeen")
    csv_file.close()

except FileNotFoundError:  # file not found exception handing, error message+exit code
    print("File Not Found")
    print("Saarim Tashfeen")
    exit()
