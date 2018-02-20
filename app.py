import datetime
import os
from xero.auth import PublicCredentials
from xero import Xero


try:
    key = os.environ['XERO_CONSUMER_KEY']
except KeyError:
    print("Environment variable XERO_CONSUMER_KEY not defined")
    raise

try:
    secret = os.environ['XERO_CONSUMER_SECRET']
except KeyError:
    print("Environment variable XERO_CONSUMER_SECRET not defined")
    raise

# Typically this will be loaded from a database
saved_state = None

if saved_state is not None:
    credentials = PublicCredentials(**saved_state)
else:
    credentials = PublicCredentials(key, secret)
    print(credentials.url)
    code = input("Enter the verification code: ")
    credentials.verify(code)
    saved_state = credentials.state
    print(saved_state)

xero = Xero(credentials)

contacts = xero.contacts.all()
print(contacts)

purchased_items = xero.items.filter(IsPurchased=True)
sold_items = xero.items.filter(IsSold=False)

print("Purchased Items: ")
for i in purchased_items:
    print(i['IsPurchased'])

print("----------------------------------------")

print("Sold Items: ")
for i in sold_items:
    print(i['IsSold'])
