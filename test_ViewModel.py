"""View in MVC Saarim Tashfeen"""
from unittest import TestCase

import ViewModel
from ModelCovid import Covid
from ModelCovid import CovidThread


class Test(TestCase):
    def test_printdata(self):
        thelist = []
        Covid.readdata(Covid, thelist)
        thelisttwo = []
        thread1 = CovidThread(1, "Thread-1", 1, thelisttwo)
        thread1.start()
        #ViewModel.printdata(thelist)
        ViewModel.printdata(thelisttwo)
       # self.fail()
