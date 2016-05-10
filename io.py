from usps_module import *
import os
os.system('clear')

def print_data(tracking_data):
  for detail in tracking_data:
    print ("+++" + detail)

id="9534612156126123269099" # Package sent to Alaska

print ("****** Welcome to PACTRAC-cl, your favorite package tracker. *****")
print ()
print ("     Which carrier has your parcel?")
print ("          Select 1 for United States Postal Service")
print ("          Select 2 for UPS")
print ()
carrier_selection = str(input ("     What is your selection?  "))
print ()
while carrier_selection not in ["1","2"]:
    print ("------> Warning: Selection Invalid!!")
    print ()
    carrier_selection = input ("     Please select 1 for USPS , or 2 for UPS :  ")
    print ()
if carrier_selection == "1":
  carrier = "USPS"
elif carrier_selection == "2":
  carrier = "UPS"
print ("     You have selected %s as your carrier." %(carrier))
print ()
id = input ("Please enter the package's tracking number:  ")
print()
print()
## We need some validations here, but we haven't found reliable ones yet.

if carrier == "USPS":
  tracking_data = usps_call(id)
  print_data (tracking_data)
  print ()

if carrier == "UPS":
  print ("UPS API IS UNDER CONSTRUCTION")
  print ()