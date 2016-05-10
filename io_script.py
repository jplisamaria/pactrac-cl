from APIS_module import *
from io_module import *
import os
os.system('clear')

print ("****** Welcome to PACTRAC-cl, your favorite package tracker. *****")
print ()
carrier_selection = True
while True:
  print ("     Which carrier has your parcel?")
  print ("          Enter 1 for United States Postal Service")
  print ("          Enter 2 for UPS")
  print ("          Select q or Q to quit")
  print ()
  carrier_selection = str(input ("     What is your selection?  "))
  print ()
  while carrier_selection not in ["1","2","q","Q"]:
      print ("------> Warning: Selection Invalid!!")
      print ()
      carrier_selection = input ("     Please select 1 for USPS , or 2 for UPS :  ")
      print ()
  if carrier_selection == "1":
    carrier = "USPS"
  elif carrier_selection == "2":
    carrier = "UPS"
  elif carrier_selection in ["Q", "q"]:
    print ("Thank you, come again.")
    print()
    exit()
  print ("     You have selected %s as your carrier." %(carrier))
  print ()
  id = str(input ("Please enter the package's tracking number:  "))
  ## We need some validations here, but we haven't found reliable ones yet.
  print()
  print()
  print_data(id, carrier)
  print ("     Want to track another package?  ")
  carrier_selection = input("     Enter q or Q to quit.  Hit any key to continue.  ")
  print()
  print()
  if carrier_selection  in ["q", "Q"]:
    print ("Thank you, come again.")
    print ()
    exit()
