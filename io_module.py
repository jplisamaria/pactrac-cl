from APIS_module import *
from io_module import *

def print_data(id, carrier):
  if carrier == "USPS":
    tracking_data = usps_call(id)
  elif carrier == "UPS":
    tracking_data = ups_call(id)
  print ("%s package %s" %(carrier, id))
  print ("-" * len("%s package %s" %(carrier, id)) )
  for detail in tracking_data:
    print ("+++ " + detail)
  print ()
