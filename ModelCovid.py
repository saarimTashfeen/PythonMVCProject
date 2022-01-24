"""Model in MVC Saarim Tashfeen"""
#Author: Saarim Tashfeen
#CST8333

import csv
import threading


class CovidThread (threading.Thread):
   """Class to implement threading module"""
   def __init__(self, list):
      threading.Thread.__init__(self)
      self.list = list
   def run(self):
      print("Starting therad")
      print("before reading data")
      Covid.readdata(Covid, self.list)
      print("after reading data")
      print("Ending")
      return self.list



class Covid(object):

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

    def readdata(self, list):
        """Reads dataset and initializes objects, returns list"""
        counter = 0  # counter for the loop when reading file
        try:
            with open('covid19-download.csv') as csv_file:  # Saarim Tashfeen
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # skips the first line of file, (column names)

                for row in csv_reader:  # Saarim Tashfeen
                    list.append(Covid(row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[13], row[15]))
                    # row[0], row[1] etc... reading columns we are only insterested in A,B,C,D,F etc...
                    counter += 1
                    if counter == 100:  # after 100 lines, break fom loop
                        break
             #for Covid in list:
              #  print(Covid)

            #  print("Saarim Tashfeen")
            csv_file.close()
            return list

        except FileNotFoundError:  # file not found exception handing, error message+exit code
            print("File Not Found")
            print("Saarim Tashfeen")
            exit()

    def write(self, list):
        """Enter new data entry into list"""
        with open('newfile.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ["pruid", "prname", "prnamefr", "date", "numconf", "numprob", "numdeaths", "numtotal", "numtoday",
                 "ratetotal"])

            for Covid in list:
                writer.writerow([Covid.pruid, Covid.prname, Covid.prnamefr, Covid.date, Covid.numconf, Covid.numprob,
                                 Covid.numdeaths, Covid.numtotal, Covid.numtoday, Covid.ratetotal])


    def edit(self, list, editone, edittwo, editthree):
        """Edit entry based on user input"""
        if edittwo == '1':
            list[editone].pruid = editthree
        elif edittwo == '2':
            list[editone].prname = editthree
        elif edittwo == '3':
            list[editone].prnamefr = editthree
        elif edittwo == '4':
            list[editone].date = editthree
        elif edittwo =='5':
            list[editone].numconf = editthree
        elif edittwo =='6':
            list[editone].numprob = editthree
        elif edittwo =='7':
            list[editone].numdeaths = editthree
        elif edittwo =='8':
            list[editone].numtotal = editthree
        elif edittwo =='9':
            list[editone].numtoday = editthree
        elif edittwo =='10':
            list[editone].ratetotal = editthree
        return list

    def delete(self, list, deletenumber):
        """Delete record according to user input, return list"""
        list.pop(int(deletenumber))
        return list
