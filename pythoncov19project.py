from tkinter.ttk import *    
from tkinter import *
from tkinter import messagebox
import urllib.request,urllib.parse,urllib.error
import json,datetime
from datetime import timedelta
import re
import ssl
def submit():
    pattern_state=r"[A-z]+"
    pattern_date=r"[\d]{4}-[\d]{2}-[\d]{2}"
    state_get=state_entry.get().upper()
    date_get=date_entry.get()  
    if re.match(pattern_state,state_get)==None:
        messagebox.showinfo("Error","Enter State")  
    if re.match(pattern_date,date_get)==None:
        messagebox.showinfo("Error","Date Format:YYYY//MM//DD")
    if state_get not in states and state_get!="":
        messagebox.showinfo("Error","Not a state in India")        
    print(state_get,date_get)
    urll="https://data.covid19india.org/v4/min/data.min.json"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url=urllib.request.urlopen(urll, context=ctx).read()
    data=json.loads(url)
    display.delete(1.0,END)
    display.insert(END,state_get,date_get,"\n")
    display.insert(END,"State Code : ")
    display.insert(END,states[state_get]+"\n")
    #for x,y in data[states[state_get]]['dates'][date_get]['total'].items():
    for i in data[states[state_get]]['total']:
            print(i)
            print(data[states[state_get]]['total'][i])
            display.insert(END,(i,data[states[state_get]]['total'][i])) 
            display.insert(END,"\n")
        #print(states[state_get])     
root=Tk()
states={'ANDAMAN AND NICOBAR ISLANDS':"AN","ANDHRA PRADESH":"AP","ARUNACHAL PRADESH":"AR","ASSAM":"AS","BIHAR":"BR",
"CHANDIGARH":"CH","CHHATTISGARH":"CT","DADRA AND NAGAR HAVELI":"DN","DAMAN AND DIU":"DD","DELHI":"DL","GOA":"GA",
"GUJURAT":"GJ","HARYANA":"HR","HIMACHAL PRADESH":"HP","JAMMU AND KASHMIR":"JK","JHARKHAND":"JH","KARNATAKA":"KA",
"KERALA":"KL","LAKSWADEEP":"LD","MADHYA PRADESH":"MP","MAHARASHTRA":"MH","MANIPUR":"MN","MEGHALAYA":"ML","MIZORAM":"MZ",
"NAGALAND":"NL","ODISHA":"OR","PUDUCHERRY":"PY","PUNJAB":"PB","RAJASTHAN":"RJ","SIKKIM":"SK","TAMILNADU":"TN","TELANGANA":"TG",
"TRIPURA":"TR","UTTAR PRADESH":"UP","UTTARAKHAND":"UT","WEST BENGAL":"WB"}
get_state=StringVar
get_date=StringVar()
root.title("Covid Cases of Any India State") 
root.geometry("500x500")
title=Label(text='Covid Information of a State',font=14)
title.place(x=120,y=10)#.grid(row=0,columnspan=2)
state=Label(text='State',font=5)
state.place(x=10,y=50)#.grid(row=1,column=0)
state_entry=Entry(root,font=2)
state_entry.place(x=100,y=55)#.grid(row=1,column=1)
date=Label(text='Date',font=5,width=5)
date.place(x=8,y=90)#.grid(row=2,column=0)
date_entry=Entry(root,font=2)
date_entry.place(x=100,y=95)#.grid(row=2,column=1)
submit=Button(text='Submit',command=submit,width=10,bg='cyan')
submit.place(x=85,y=135)#.grid(row=3,column=1)
todays_date=datetime.date.today()
yesterday=todays_date-timedelta(days=1)
#get_date.set(str(todays_date))
print(todays_date)
date_entry.insert(END,yesterday)
display=Text(root,height = 10,width = 40,bg = "light cyan",font=3)
display.place(x=25,y=200)

root.mainloop()  
