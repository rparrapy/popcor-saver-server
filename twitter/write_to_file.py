__author__ = 'rodfusion'

import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Files/Tweets.txt", "a")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass


sys.stdout = Logger()
print("Hello File!")