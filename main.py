import glob
import csv
import codecs

"""
import string
import mechanize
import cookielib
import re
import os
import sys
from time import gmtime, strftime
from random import randint
from time import sleep
from bs4 import BeautifulSoup
"""

# import private


def main():
  
  print("update-gc-art.py starting...")

  for numbers in glob.iglob('/tmp/inputs/*.csv'):
    
    if numbers.rsplit(".")[-1] != "csv":
      print("ERROR - File must have a .csv extension!  {} found.".format(numbers))
      exit(1)
      
    print("Processing CSV file {}...".format(numbers))

    with codecs.open(numbers, "rU", encoding='utf-8', errors='ignore') as csvFile:
      reader = csv.DictReader(csvFile)
      for row in reader:
        print(row['GC Code'], row['Reflected GC Code'])
    
 
if __name__ == '__main__':
    main()
