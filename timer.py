'''
Timer(Stopwatch) with laps system display in both digital label and analog clock.
'''
from Tkinter import *
import time

class Timer():
    def __init__(self):
        '''
        main
        '''
        self.start = 0.0
        self.elapsed = 0.0
        self.timedis = StringVar()
        
    def count(self):
        '''
        count() --> makes timer update every 50 millisecs // name after part for using in stop
        '''
        self.elapsed = time.time() - self.start
        self.display(self.elapsed)
        self.counter = self.after(50, self.count)

    def display(self, time):
        '''
        display(time) --> set floating point format into 00:00:00:00 format
        '''
        hrs = int(time / 3600)
        mins = int((time - hrs*3600.0) /60 )
        secs = int(time - hrs*3600.0 - mins*60.0)
        msecs = int((time - hrs*3600.0 - mins*60.0 - secs)*100)
        self.timedis.set('%02d:%02d:%02d:%02d' % (hrs, mins, secs, msecs))
        
    def start_time(self):
        if  not self.run:
                self.start = time.time() - self.elapsed
                self.count()
                self.run = True

