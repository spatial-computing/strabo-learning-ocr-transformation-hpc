__author__ = 'rmenon'

import gbc
import sys

def main(argv):
    gbc.classify(training_label=argv[0])

if __name__=="__main__":
    main(sys.argv[1:])

