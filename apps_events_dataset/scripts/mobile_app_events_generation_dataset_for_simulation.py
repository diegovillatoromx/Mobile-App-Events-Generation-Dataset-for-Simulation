import pandas as pd
import random
import time
import hashlib
from datetime import datetime

# Define lists of cities, online payment methods, operating systems, phone models, and purchase statuses
cities = ['Mexico City', 'Guadalajara', 'Monterrey', 'Puebla', 'Tijuana']
payment_online = ['Credit_card', 'Spei', 'PayPal', 'OXXO Pay']
os = ['Android_13', 'iOS_16', 'Windows_11', 'macOS_Monterey', 'Linux_Ubuntu_22.04']
final_user_event = ['PURCHASE', 'EXIT_APP', 'PURCHASE', 'EXIT_APP', 'PURCHASE']
phone_models = [
    'Samsung Galaxy S21', 'Samsung Galaxy S22', 'iPhone 13 Pro', 'iPhone 14 Pro Max',
    'Google Pixel 6', 'Google Pixel 7',
    'OnePlus 9 Pro', 'OnePlus 10 Pro',
    'Xiaomi Mi 11', 'Xiaomi Mi 12',
    'Huawei P40', 'Huawei P50',
    'Sony Xperia 5 III', 'Sony Xperia 6',
    'LG Velvet', 'LG Velvet 2',
    'Motorola Moto G Power', 'Motorola Moto G Power 2',
    'Oppo Find X3 Pro', 'Oppo Find X4 Pro'
]
purchase_statuses = [
    'COMPLETED', 'FAILED_CHECKOUT', 'FAILED_API_RESPONSE',
    'INSUFFICIENT_FUNDS', 'USER_ERROR', 'FRAUD', 'PENDING', 'CANCELLED'
]

# Define initial events, user events, and event categories
initial_event = 'LAUNCH_APP'
second_event = ['HOME', 'EXIT_APP', 'HOME']
third_event = ['GO_TO_CATEGORY', 'EXIT_APP', 'GO_TO_CATEGORY', 'GO_TO_CATEGORY']
event_category = ['ELECTRONICS', 'CLOTHING', 'FOOD', 'HOME_APPLIANCES', 'BOOKS', 'SPORTS']

# Define coordinates for cities
mexico_city_coords = (19.4326, -99.1332)
guadalajara_coords = (20.6597, -103.3496)
monterrey_coords = (25.6866, -100.3161)
puebla_coords = (19.0414, -98.2063)
tijuana_coords = (32.5149, -117.0382)

# Create a list of users beforehand
def create_massive_users(n_users):
    users_bank = []

    for i in range(n_users):
        date = pd.to_datetime('today').strftime("%Y-%m-%d %H:%M:%S")
        users_bank.append(str(hashlib.sha256(f"{i} {date}".encode('utf-8')).hexdigest())[:10])

    return users_bank


# Function to get the second event based on random choices
def get_second_event(initial_event, second_event, third_event, os, cities):
    event_2 = random.choice(second_event)
    if event_2 == 'HOME':
        event_3 = random.choice(third_event)
        if event_3 == 'GO_TO_CATEGORY':
            last_event = random.choice(event_category)
            final_event = random.choice(final_user_event)
            if final_event == 'PURCHASE':
                payment = random.choice(payment_online)
                os_source = random.choice(os)
                city = random.choice(cities)
                status = 'COMPLETED'
                order_type = 'PURCHASE'
            elif final_event == 'EXIT_APP':
                payment = 'Null'
                os_source = random.choice(os)
                city = random.choice(cities)
                status = 'UNCONVERTED'
                order_type = 'USER_VISIT'
        elif event_3 == 'EXIT_APP':
            payment = 'Null'
            os_source = random.choice(os)
            city = random.choice(cities)
            status = 'UNCONVERTED'
            order_type = 'USER_VISIT'
            last_event = 'HOME'
    else:
        payment = 'Null'
        os_source = random.choice(os)
        city = random.choice(cities)
        status = 'UNCONVERTED'
        order_type = 'USER_VISIT'
        last_event = 'LAUNCH_APP'
        event_3 = 'Null'
    return initial_event, event_2, event_3, last_event, os_source, city, order_type, status, payment

# Function to get coordinates of a city
def get_coords(city):
    if city == 'Mexico City':
        coords = mexico_city_coords
    elif city == 'Guadalajara':
        coords = guadalajara_coords
    elif city == 'Monterrey':
        coords = monterrey_coords
    elif city == 'Puebla':
        coords = puebla_coords
    elif city == 'Tijuana':
        coords = tijuana_coords
    return coords

# Function to generate simulated data
def generate_simulated_data(num_records, num_users):
    # Create a list of random users
    user_list = create_massive_users(num_users)

    user_purchase_count = {}
    data_purchase = []
    x = 0

    while x < num_records:
        date = pd.to_datetime('today').strftime("%Y-%m-%d %H:%M:%S")
        event = get_second_event(initial_event, second_event, third_event, os, cities)
        user_id = random.choice(user_list)  # Randomly select a user from the list
        event_user_1 = event[0]
        event_user_2 = event[1]
        event_user_3 = event[2]
        event_user_4 = event[3]
        event_user_os = event[4]
        event_user_city = event[5]
        event_user_order = event[6]
        event_user_status = event[7]
        event_user_payment = event[8]

        # Get the current hour and day
        current_hour = datetime.now().hour
        current_day = datetime.now().day

        # Update user's purchase count for the current hour and day
        if user_id not in user_purchase_count:
            user_purchase_count[user_id] = {'hourly_count': {current_hour: 1}, 'daily_count': {current_day: 1}}
        else:
            if current_hour in user_purchase_count[user_id]['hourly_count']:
                user_purchase_count[user_id]['hourly_count'][current_hour] += 1
            else:
                user_purchase_count[user_id]['hourly_count'][current_hour] = 1

            if current_day in user_purchase_count[user_id]['daily_count']:
                user_purchase_count[user_id]['daily_count'][current_day] += 1
            else:
                user_purchase_count[user_id]['daily_count'][current_day] = 1

        purchase = {'USER_ID': user_id,
                    'INITIAL_EVENT': event_user_1,
                    'EVENT_2': event_user_2,
                    'EVENT_3': event_user_3,
                    'EVENT_OUT': event_user_4,
                    'OS_USER': event_user_os,
                    'CITY': event_user_city,
                    'LATITUDE': get_coords(event_user_city)[0],
                    'LONGITUDE': get_coords(event_user_city)[1],
                    'ORDER_TYPE': event_user_order,
                    'STATUS': event_user_status,
                    'PAYMENT_METHOD': event_user_payment,
                    'CREATED_AT': date,
                    'HOURLY_PURCHASE_COUNT': user_purchase_count[user_id]['hourly_count'].get(current_hour, 0),
                    'DAILY_PURCHASE_COUNT': user_purchase_count[user_id]['daily_count'].get(current_day, 0)}

        data_purchase.append(pd.DataFrame(purchase, index=[x]))
        #print(purchase)
        x += 1
        time.sleep(random.choice([1, 1.5, 2]))

    return pd.concat(data_purchase, ignore_index=True)

# Generate simulated data (you can specify the number of records and users)
simulated_data = generate_simulated_data(num_records=100, num_users=1000)

# Convert the data to a Pandas DataFrame
df_simulated_data = pd.DataFrame(simulated_data)

print(df_simulated_data.head())

df_simulated_data.to_csv('simulated_data.csv', index=False)

