import csv
import logging
import sys
import json
import os.path

logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

logging.info('Program Start')

task = input("Select All to view balances, or type a name to see their transaction:\n")

logging.info("The task '" + task + "' was selected")

logging.info("Opening the file...")

#extension = os.path.splitext(file)[1]

file = input("Input the file:\n")

extension = os.path.splitext(file)[1]


if extension == ".json":
    with open(file) as f:
        data = json.load(f)
        for item in data:
            item["Date"] = item.pop("date")
            item["From"] = item.pop("fromAccount")
            item["To"] = item.pop("toAccount")
            item["Narrative"] = item.pop("narrative")
            item["Amount"] = str(item.pop("amount"))

if extension == ".csv":
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

accounts = {}


logging.info("Begin data extraction...")

for transaction in data:
    try:
        if transaction["From"] not in accounts:
            accounts[transaction["From"]] = - float(transaction["Amount"])
        else:
            accounts[transaction["From"]] -= float(transaction["Amount"])

        if transaction["To"] not in accounts:
            accounts[transaction["To"]] = float(transaction["Amount"])
        else:
            accounts[transaction["To"]] += float(transaction["Amount"])

    except:
        e = sys.exc_info()
        logging.info((e))

if task == "All":
    for name in accounts:
        print(name, round(accounts[name], 2))

if task in accounts:
    for trans in data:
        if trans["From"] == task or trans["To"] == task:
            print(trans["From"]+" paid", trans["To"], "£"+trans["Amount"], "for "+trans["Narrative"], "on "+trans["Date"])
