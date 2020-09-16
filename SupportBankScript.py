import csv
import logging

logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

logging.info('Program Start')

task = input("Select All to view balances, or type a name to see their transaction:\n")

logging.info("The task '" + task + "' was selected")

logging.info("Opening the file...")

with open('DodgyTransactions2015.csv', newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

accounts = {}


logging.info("Begin data extraction...")

for transaction in data:
    if transaction["From"] not in accounts:
        accounts[transaction["From"]] = - float(transaction["Amount"])
    else:
        accounts[transaction["From"]] -= float(transaction["Amount"])

    if transaction["To"] not in accounts:
        accounts[transaction["To"]] = float(transaction["Amount"])
    else:
        accounts[transaction["To"]] += float(transaction["Amount"])

if task == "All":
    for name in accounts:
        print(name, round(accounts[name], 2))

if task in accounts:
    for trans in data:
        if trans["From"] == task or trans["To"] == task:
            print(trans["From"]+" paid", trans["To"], "£"+trans["Amount"], "for "+trans["Narrative"], "on "+trans["Date"])
