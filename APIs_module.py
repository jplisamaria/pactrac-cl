from xml.etree import ElementTree as ET
import urllib.request, urllib.error, urllib.parse
import xml.dom.minidom
import cgi, cgitb


def api_call(id, carrier):
  if carrier == "USPS":
    tracking_data = __usps_call(id)
  elif carrier == "UPS":
    tracking_data = __ups_call(id)
  elif carrier == "FedEx":
    tracking_data = __fedex_call(id)
  return (tracking_data)

def __ups_call(id):
    return (['UPS API IS UNDER CONSTRUCTION'])

def __fedex_call(id):
    return (['FEDEX API IS UNDER CONSTRUCTION'])

def __usps_call(id):
    #URI for API
    url = 'http://production.shippingapis.com/Shipping.dll?API=TrackV2&'
    #XML data to wrap around tracking id
    xml_start='XML=<TrackRequest USERID="586USTGL6982"><TrackID ID="'
    xml_end='"></TrackID></TrackRequest>'

    #construct XML data
    xml_data = xml_start + id + xml_end

    #encode information for post request
    data = xml_data.encode('UTF-8')

    #create request and add headers
    req = urllib.request.Request(url, data)
    req.add_header("Accept", "*/*")
    req.add_header("Content-Type","application/xml; charset=utf-8")

    #create the call to the API
    response = urllib.request.urlopen(req)

    #save the response from the API call
    response_html = response.read()
    dom = xml.dom.minidom.parseString( response_html.decode())

    #obtain the value from the TrackSummary tag
    summary = dom.getElementsByTagName("TrackSummary")
    details_list=[]
    for each in summary:
        statement = ("".join(summary[0].firstChild.nodeValue))
        details_list.append(statement)

    #obtain the value(s) from the TrackDetail tag(s)
    details = dom.getElementsByTagName("TrackDetail")
    for detail in details:
        statement =  __getText(detail.childNodes)
        details_list.append(statement)
    return details_list

#function to parse text from nodes
def __getText(nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)
