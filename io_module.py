from APIs_module import *
from io_module import *
import csv, os

def get_carrier(selection):
  if selection == "1":
    carrier = "USPS"
  elif selection == "2":
    carrier = "UPS"
  elif selection == "3":
    carrier = "FedEx"
  return carrier

def print_data(id, carrier):
  tracking_data = api_call(id, carrier)
  tracking_string = "\n"
  print ("%s package %s" %(carrier, id))
  tracking_string += ("%s package %s \n" %(carrier, id))
  print ("-" * len("%s package %s \n" %(carrier, id)) )
  tracking_string += (("-" * len("%s package %s" %(carrier, id)) ) + "\n")
  for detail in tracking_data:
    print ("+++ " + detail)
    tracking_string += ("+++ " + detail + "\n")
  print ()
  tracking_string += ("\n")
  return tracking_string

def process_csv(file):
  input_csv = open(file, "r")
  #need to add error handling if file not found
  reader = csv.reader(input_csv)
  os.system('clear')
  output_log = open("tracking_log.txt","w")
  #would like to add tracking_log.csv
  for row in reader:
    carrier = str(row[0])
    id = str(row[1])
    if carrier not in ["USPS", "UPS", "FedEx", "FEDEX", "Fedex"]:
      print ("--> Invalid Carrier!!")
      print ("Package %s not tracked." %(id))
      print()
      print()
    else:
      if carrier in ["FedEx", "FEDEX", "Fedex"]:
        carrier = "FedEx"
      output_log.write(print_data(id, carrier))
      #print_data(id, carrier)
      print()
