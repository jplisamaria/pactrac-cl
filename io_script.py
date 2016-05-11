from io_module import *
import csv
import os

os.system('clear')
print()
print ("****** Welcome to PACTRAC-cl, your favorite package tracker. *****")
print ()
while True:
  print ("     Which carrier has your parcel?")
  print ("          Enter 1 for United States Postal Service")
  print ("          Enter 2 for UPS")
  print ("          Enter 3 for FedEx")
  print ("          Enter f for csv file.")
  print ("          Enter q to quit")
  print ()
  carrier_selection = str(input ("     What is your selection?  "))
  print ()
  while carrier_selection not in ["1","2","3", "f", "F","q","Q"]:
      print ("------> Warning: Selection Invalid!!")
      print ()
      carrier_selection = input ("     Please select 1 for USPS , 2 for UPS, 3 for FedEx, f for csv file, or q to quit :  ")
      print ()
  if carrier_selection in ["Q", "q"]:
    print ("Thank you, come again.")
    print()
    exit()
  if carrier_selection in ["f", "F"]:
    print ("Enter name of csv file.  Please note that each line must be in the form of ")
    print ("                valid_carrier_name, tracking_number  ")
    filename = str(input("Filename ?  "))
    print()
    process_csv(filename)
    exit()
  carrier = get_carrier(carrier_selection)
  print ("     You have selected %s as your carrier." %(carrier))
  print ()
  id = str(input ("Please enter the package's tracking number:  "))
  ## We need some validations here, but we haven't found reliable ones yet.
  print()
  print()
  print_data(id, carrier)
  carrier_selection = input("     Enter q to quit.  Hit any key to track another package.  ")
  print()
  print()
  if carrier_selection  in ["q", "Q"]:
    print ("Thank you, come again.")
    print ()
    exit()
  else:
    os.system('clear')
    print()
