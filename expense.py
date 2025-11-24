# Personal Expense Tracker

import json
import os
from datetime import datetime

f = "expenses.json"

def loadData():
    if os.path.exists(f):
        try:
            ff = open(f,"r")
            return json.loads(ff.read())
        except:
            return []
    return []

def saveData(d):
    o = open(f,"w")
    o.write(json.dumps(d))
    o.close()

def dFix(x):
    if x.strip()=="":
        return datetime.now().strftime("%Y-%m-%d")
    fmts=["%Y-%m-%d","%d-%m-%Y","%d/%m/%Y"]
    for m in fmts:
        try:
            return datetime.strptime(x,m).strftime("%Y-%m-%d")
        except:
            pass
    return datetime.now().strftime("%Y-%m-%d")

def addExp(d):
    print("\nAdding a new expense")
    amt = float(input("Amount: "))
    c = input("Category: ")
    n = input("Note: ")
    dt1 = input("Date: ")
    dt = dFix(dt1)

    idx = d[-1]["id"]+1 if len(d)>0 else 1
    d.append({"id":idx,"amount":amt,"category":c,"note":n,"date":dt})
    saveData(d)
    print("Saved.")

def show(d):
    print("\nYour Expense List:")
    if len(d)==0:
        print("No records found.")
        return
    for i in d:
        print(str(i["id"])+" | "+i["date"]+" | "+i["category"]+" | "+str(i["amount"])+" | "+i["note"])

def removeExp(d):
    print("\nRemove Expense")
    try:
        r = int(input("Enter ID: "))
    except:
        print("Error reading ID.")
        return d
    nd=[]
    fl=0
    for i in d:
        if i["id"]==r:
            fl=1
        else:
            nd.append(i)
    if fl:
        saveData(nd)
        print("Deleted.")
        return nd
    print("ID not found.")
    return d

def catSum(d):
    print("\nCategory Totals:")
    ss={}
    for i in d:
        if i["category"] not in ss:
            ss[i["category"]] = i["amount"]
        else:
            ss[i["category"]] += i["amount"]
    for a,b in ss.items():
        print(a, b)

def tot(d):
    print("\nTotal Spent:")
    t = 0
    for i in d:
        t += i["amount"]
    print(t)

def main():
    d = loadData()
    print("======== Personal Expense Tracker ========")

    while True:
        print("\n1.Add  2.View  3.Delete  4.CatTotal  5.Total  6.Exit")
        c = input("> ")
        if c=="1":
            addExp(d)
        elif c=="2":
            show(d)
        elif c=="3":
            d = removeExp(d)
        elif c=="4":
            catSum(d)
        elif c=="5":
            tot(d)
        else:
            break

main()
