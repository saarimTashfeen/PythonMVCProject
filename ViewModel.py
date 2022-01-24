"""View in MVC model"""
#Author: Saarim Tashfeen
#CST8333

from ModelCovid import Covid
from ascii_graph import Pyasciigraph #library for charting


def chart(list):
    "charts selected data"

    #Saarim Tashfeen

    chartnumber = int(input(" Enter which record you want to chart")) #userinput for what record

    datatochart = [('Confirmed Cases', int(list[(chartnumber)].numconf)),
                   ('Number of Deaths', int(list[chartnumber].numdeaths)),
                    ('Total Numbers', int(list[chartnumber].numtotal)),
                    ('Numbers Today', int(list[chartnumber].numtoday))]

    graph = Pyasciigraph() #pyasciigraph object
    for line in graph.graph('Chart Data', datatochart): #loop that actually charts out data
        print(line)


def start():
    """ Start program and list initial options"""
    print("Saarim Tashfeen")
    print("Program has started")
    print("Press r to reload/load data")
    print("Press w to write current data in list to new file")


def options():
    """All possile options"""
    print("Saarim Tashfeen")
    print("Press r to reload/load data from dataset")
    print("Press l to print in memory data")
    print("Press w to write current data in list to new file")
    print("Press s to select one record to display")
    print("Press a to select multiple records list to display")
    print("Press c to create record")
    print("Press e to edit record")
    print("Press d to delete record")
    print("Press k to chart data")

def printdata(list):
    """prints list"""
    for Covid in list:
        print(Covid)

def selectrecord(list):
    """Select one record"""
    numberView = input("enter the number of the data entry you want to display")
    print(list[int(numberView)])

def selectrecords(list):
    """Select multiple records"""
    i = 0
    recnumber = []
    numberViewOne = input("Enter the amount of records you want displayed")
    while i < int(numberViewOne):
        recnumber += input("Enter the records you want displayed")
        i += 1

    x = 0
    while x < len(recnumber):
        print(list[int(recnumber[x])])
        x += 1

def create(list):
    """Retrive user data and enter new record"""
    print("enter details for new record")
    pruid = input("Province ID")
    prname = input("Province Name")
    prnamefr = input("Province Name French")
    date = input("Date")
    numconf = input("Numconf")
    numprob = input("Numprob")
    numdeaths = input("Numdeaths")
    numtotal = input("Numtotal")
    numtoday = input("Numtoday")
    ratetotal = input("Ratetotal")
    list.append(Covid(pruid, prname, prnamefr, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal))

def editone():
    """Return whih entry is being edited"""
    editone = int(input("Enter number of entry you want to edit"))
    return editone

def edittwo():
    """Return what attribute user wants to edit"""
    edittwo = input("Enter the attribute you want to edit 1-10, 1 being pruid.")
    return edittwo

def editthree():
    """Return user edit"""
    editthree = input("Enter your edit")
    return editthree

def viewdelete():
    """Return which entry user wants to delete"""
    deletenumber = input("which record in the sequential structure do you want to delete")
    return deletenumber



