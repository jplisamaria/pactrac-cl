from APIs_module import *
from io_module import *

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
  print ("%s package %s" %(carrier, id))
  print ("-" * len("%s package %s" %(carrier, id)) )
  for detail in tracking_data:
    print ("+++ " + detail)
  print ()
