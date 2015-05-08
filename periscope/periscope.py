#!/usr/bin/env python
import tests
import gui

class Periscope:
    def __init__(self):
        self.TestManager = tests.TestManager()
        self.gui = gui.gui(self)

if __name__ == '__main__':
    periscope = Periscope()
