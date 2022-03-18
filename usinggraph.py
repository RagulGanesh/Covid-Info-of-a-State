import urllib.request,urllib.parse,urllib.error
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
import ssl
urll="https://data.covid19india.org/v4/min/data.min.json"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=urllib.request.urlopen(urll, context=ctx).read()
data=json.loads(url)
#for x,y in data.items():
#    print(x,y)
#print(data['ML']['dates'])
#for i in data['ML']['dates']:
#    print(i)
#for x,y in data['ML']['dates']['2021-08-23']['total'].items(): 
#    print(x,y) 
states={'ANDAMAN AND NICOBAR ISLANDS':"AN","ANDHRA PRADESH":"AP","ARUNACHAL PRADESH":"AR","ASSAM":"AS","BIHAR":"BR",
"CHANDIGARH":"CH","CHHATTISGARH":"CT","DADRA AND NAGAR HAVELI":"DN","DAMAN AND DIU":"DD","DELHI":"DL","GOA":"GA",
"GUJURAT":"GJ","HARYANA":"HR","HIMACHAL PRADESH":"HP","JAMMU AND KASHMIR":"JK","JHARKHAND":"JH","KARNATAKA":"KA",
"KERALA":"KL","LAKSWADEEP":"LD","MADHYA PRADESH":"MP","MAHARASHTRA":"MH","MANIPUR":"MN","MEGHALAYA":"ML","MIZORAM":"MZ",
"NAGALAND":"NL","ODISHA":"OR","PUDUCHERRY":"PY","PUNJAB":"PB","RAJASTHAN":"RJ","SIKKIM":"SK","TAMILNADU":"TN","TELANGANA":"TG",
"TRIPURA":"TR","UTTAR PRADESH":"UP","UTTARAKHAND":"UT","WEST BENGAL":"WB"}
todays_date=datetime.date.today()
yesterday=todays_date-timedelta(days=1)  
state_list=[]
for i in data:
    if i=='UN' or i=='TT': continue
    state_list.append(i)
#print(state_list)
#print(data['UP']['dates']['2021-08-23']['total']['confirmed']) 
confirmed_list=[]
for i in data:
    #print(i)
    if i=='UN' or i=='TT': continue
    #print(i,data[i]['dates']['2021-08-23']['total']['confirmed'])
    #confirmed_list.append(data[i]['dates'][str(yesterday)]['total']['confirmed'])
    confirmed_list.append(data[i]['total']['confirmed'])
    pass
#print(confirmed_list)
x=np.array(state_list)
y=np.array(confirmed_list)
plt.bar(x,y)
plt.title("Confirmed Cases for Various States"+" as of  "+str(yesterday))
plt.xlabel("State Codes")
plt.ylabel("Confirmed Cases")
#plt.grid()
plt.show()