import time
import csv
import random
from datetime import datetime
from faker import Faker
from faker.providers import BaseProvider
import pandas as pd

fakeData = Faker()

####

parcels = [random.randint(1000000000, 2147483647) for i in range(270)]


consumer_ids = []
agent_ids = []
built = {}
transaction_id = 100000000
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com', 'msn.com']

# Consumers
def generate_consumer_id():
    id = random.randint(100000000, 999999999)
    if id not in consumer_ids:
        consumer_ids.append(id)
        return id
    else:
        return generate_consumer_id()

def generate_name_email():
    first = fakeData.first_name()
    last = fakeData.last_name()
    return first + " " + last, first + '.' + last + "@" + random.choice(email_domains)

def generate_phone():
    area = random.randint(100, 999)
    prefix = random.randint(100, 999)
    suffix = random.randint(1000, 9999)
    return '(' + str(area) + ')' + ' ' + str(prefix) + '-' + str(suffix)

def generate_goal():
    return random.choice(['buy', 'sell'])

def pref_property():
    return random.choice(parcels)

# Properties
# def generate_parcel():
#     parcel = random.randint(1000000000, 2147483647)
#     if parcel not in parcels:
#         parcels.append(parcel)
#         return parcel
#     else:
#         return generate_parcel()

# def generate_address():
#     return fakeData.street_address()

# def generate_city():
#     return fakeData.city()

# def generate_state():
#     return fakeData.state_abbr()

# def generate_zip():
#     return fakeData.postcode()

# def generate_year():
#     return fakeData.year()

# def generate_style():
#     return random.choice(['ranch', 'modern', 'colonial', 'dutch', 'bungalow', 'victorian', 'contemporary', 'cottage'])

# def generate_rooms(stories):
#     if (stories == 1):
#         return random.randint(4, 8)
#     elif (stories == 2):
#         return random.randint(6, 12)
#     else:
#         return random.randint(10, 20)

def generate_date(parcel):
    year = random.randint(2000, 2023)
    month = fakeData.month()
    day = random.randint(1, 28)
    return f'{year}-{month}-{day}'

# Agents
with open('agents.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['agentID', 'name', 'phone', 'email', 'commission'])
    for i in range(0, 50):
        ID = random.randint(100000000, 900000000)
        NE = generate_name_email()
        if ID not in agent_ids:
            myagent = [ID, NE[0], generate_phone(), NE[1], round(random.uniform(4.0, 7.0), 2)]
            writer.writerow(myagent)
            agent_ids.append(ID)

# Properties
# with open('property_data.csv', 'w', newline = '') as csvfile:
#     writer = csv.writer(csvfile)
#     # writer.writerow(['parcel', 'address', 'city', 'state', 'zip', 'year_built', 'bedrooms', 'bathrooms', 'total_rooms', 'last_year_tax_amount', 'square_feet', 'style', 'stories', 'estimated_value', 'agent'])
#     for i in range(1000):
#         parcel = generate_parcel()
#         address = generate_address()
#         city = generate_city()
#         state = generate_state()
#         zip = generate_zip()
#         year_built = generate_year()
#         built[parcel] = year_built
#         stories = random.randint(1, 3)
#         rooms = generate_rooms(stories)
#         bedrooms = random.randint(1, rooms-3)
#         bathrooms = random.randint(1, rooms-bedrooms-2)
#         tax = round(random.uniform(0.3, 3), 2)
#         square_feet = random.randint(1250, 4000)
#         style = generate_style()
#         estimated_value = round(random.uniform(300000, 2000000), 2)
#         agent = random.choice(agent_ids)
#         writer.writerow([parcel, address, city, state, zip, year_built, bedrooms, bathrooms, rooms, tax, square_feet, style, stories, estimated_value, agent])

# Consumer
with open('consumer_data.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['consumerID', 'name', 'phone', 'goal', 'email', 'preferred_property'])
    for i in range(500):
        id = generate_consumer_id()
        name_email = generate_name_email()
        phone = generate_phone()
        goal = generate_goal()
        preferred = pref_property()
        writer.writerow([id, name_email[0], phone, goal, name_email[1], preferred])

# Transactions
with open('transaction_data.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['transactionID', 'agent', 'consumer', 'property', 'sale_price', 'sale_date'])
    for i in range(300):
        tid = transaction_id
        a = random.choice(agent_ids)
        c = random.choice(consumer_ids)
        p = random.choice(parcels)
        price = round(random.uniform(300000, 2000000), 2)
        sell_date = generate_date(p)
        writer.writerow([tid, a, c, p, price, sell_date])
        transaction_id += 1
