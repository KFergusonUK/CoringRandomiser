import fnmatch
import os
import csv
import random
rowcount = 0
count=0
compiledlist = []

def run():

    try:
        for file in os.listdir('.'):
            if fnmatch.fnmatch(file, '*.csv'):
                print("File " + file + " detected in folder. \n")
                print("Processing file...\n\n")
    except:
            print("Error in loading file, please ensure you place only one .csv file in the folder with this program.")

    try:        
        # open upload and check file for reading.
        promotor = input ("Please enter promotor name (as it appears on Street Manager). \ne.g. BT, VIRGIN MEDIA, NORTHUMBRIAN WATER, NORTHERN POWERGRID (NORTHEAST) PLC, NORTHERN GAS NETWORKS, Netomnia Limited: \nEnter r to select at random, from any promotor: ")
        with open(file, encoding='utf-8', newline='') as smexport:

              filtered = (line.replace('\r', '') for line in smexport)

              for row in csv.reader(filtered):
                  if row[5] == promotor and row[10] == "Category B" and row[14] == "Passed": 
                      compiledlist.append(row[1])
                  elif promotor == "r" and row[10] == "Category B" and row[14] == "Passed": 
                      compiledlist.append(row[1])
                      pass
              r = random.choice(compiledlist)
              print(r)
              try:
                  with open('Coring.txt', 'a') as f:
                      f.write(r + ", ")
                      print("Results written to Coring.txt file.")
              except:
                  print("Error occured, please ensure file 'Coring.txt' exists within this folder.") 
                     
    except IndexError as error:
            print("The file in this folder does not contain the expected amount of entires, the work promotoer name was not as printed in Street Manager, or the .csv file is missing, please ensure you have only placed one Street Manager (Applications and Works) export file in this folder.")
    except:
            print("Error encountered, please ensure the folder contains the Street Manager Export file. Shutting down.")

    again = input("\nDo you wish to generate another (y/n)?")
    if again == "y" or again == "Y" or again == "yes" or again == "Yes":
        run()
    elif again == "n" or again == "N" or again == "no" or again == "No":
        input("\nPress enter key to exit.")
    else:
        input("\nY or N expected as input. Press enter key to exit.")

run()
