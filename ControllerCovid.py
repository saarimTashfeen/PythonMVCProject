"""Controller in MVC Saarim Tashfeen"""
#Author: Saarim Tashfeen
#CST8333

from ModelCovid import Covid
from ModelCovid import CovidThread
import ViewModel

import csv

list=[]

def contreaddata():
    """Delegate function to Covid"""
    #Covid.readdata(Covid, list)
    thread1 = CovidThread(list) #create the thread
    thread1.start() #start the thread
    #return ViewModel.printdata(list)

def contwrite():
    """Delegate function to Covid"""
    Covid.write(Covid, list)

def conedit(editone, edittwo, editthree):
    """Delegate function to Covid"""
    Covid.edit(Covid, list, editone, edittwo, editthree)

def contdelete(list, deletenumber):
    """Delegate function to Covid"""
    Covid.delete(Covid, list, deletenumber)


"""def write():
    with open('newfile.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["pruid", "prname", "prnamefr", "date", "numconf", "numprob", "numdeaths", "numtotal", "numtoday", "ratetotal"])

        for Covid in list:
            writer.writerow([Covid.pruid, Covid.prname, Covid.prnamefr, Covid.date, Covid.numconf, Covid.numprob, Covid.numdeaths, Covid.numtotal, Covid.numtoday, Covid.ratetotal])"""

uinput = None

def startup():
    """Main decision loop for user, execute appropriate function accordingly"""
    ViewModel.start()
    uinput = input("Enter Letter")
    print("in controller")
    while uinput != 'q':
        if uinput == 'r':
            contreaddata()
        elif uinput =='l':
            ViewModel.printdata(list)
        elif uinput == 'w':
            contwrite()
        elif uinput =='s':
           ViewModel.selectrecord(list)
        elif uinput =='a':
            ViewModel.selectrecords(list)
        elif uinput =='c':
            ViewModel.create(list)
        elif uinput =='t':
            printtest(list)
        elif uinput =='e':
            editone = ViewModel.editone()
            edittwo = ViewModel.edittwo()
            editthree = ViewModel.editthree()
            conedit(editone, edittwo, editthree)
        elif uinput =='d':
            deletenumber = ViewModel.viewdelete()
            contdelete(list, deletenumber)
        elif uinput =='k':
            ViewModel.chart(list)
        else:
            print("invalid input")
        ViewModel.options()
        uinput = input("Enter Letter")

    print("Quit Program")

def printtest(list):
    "Prints the list for testing purposes"
    x = input("input")
    #print(list[0].pruid)
    list[0].pruid = '69'
    #list.pop(0)

startup()












#contreaddata()
#selectrecord(1)

