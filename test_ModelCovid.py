import threading
from unittest import TestCase
from ModelCovid import Covid
from ModelCovid import CovidThread
import ViewModel



class TestCovid(TestCase):

    def test_delete(self):
        thelist = ['John', 'smith']
        thelist.append('Saarim')
        Covid.delete(Covid, thelist, 2)

        self.assertEqual(len(thelist), 2)


class TestmyThread(TestCase):
    def test_run(self):
        thelist=[]
        Covid.readdata(Covid, thelist)
        thelisttwo=[]
        threadLock = threading.Lock()
        threads = []
        thread1 = CovidThread(thelisttwo)
        thread1.start()
        threads.append(thread1)
        for t in threads:
            t.join()
        self.assertEqual(len(thelist), len(thelisttwo))

    def test_run2(self):
        thelist = []
        Covid.readdata(Covid, thelist)
        thelisttwo = []
        threadLock = threading.Lock()
        threads = []
        thread1 = CovidThread(thelisttwo)
        thread1.start()
        threads.append(thread1)
        for t in threads:
            t.join()
        self.assertEqual(print(thelist[50]), print(thelisttwo[50]))




