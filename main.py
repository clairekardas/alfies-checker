import requests
import os
import time

# Pushover API credentials
PUSHOVER_USER_KEY = os.getenv('PUSHOVER_USER_KEY')
PUSHOVER_API_TOKEN = os.getenv('PUSHOVER_API_TOKEN')

# Alfies API endpoint
ALFIES_API_URL = 'https://api.alfies.at/api/v1/basket/products'

# Headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_5; like Mac OS X) AppleWebKit/533.22 (KHTML, like Gecko)  Chrome/54.0.2150.358 Mobile Safari/601.7',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.alfies.at/',
    'Content-Type': 'application/json',
    'Authorization': f'Token {ALFIES_AUTH_TOKEN}',
    'Origin': 'https://www.alfies.at',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
}

# List of products to check
PRODUCTS = [
    {"id": 345667, "name": "Rettersackerl Veggie"},
    {"id": 345668, "name": "Rettersackerl Fleisch"},
    # Add more products as needed
]

# Interval between each check (in seconds)
CHECK_INTERVAL = 60

# Pause duration after a product becomes available (in seconds)
PAUSE_DURATION = 3600  # 1 hour

def check_stock(product):
    payload = {
        'id': product["id"],
        'quantity': 1,
        'affiliateId': None
    }
    response = requests.post(ALFIES_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        if 'status' in data and data['status'] == 'Open':
            return True
    return False

def send_notification(product_name):
    message = f"{product_name} is available! Purchase now."
    data = {
        'token': PUSHOVER_API_TOKEN,
        'user': PUSHOVER_USER_KEY,
        'message': message,
    }
    requests.post("https://api.pushover.net/1/messages.json", data=data)

def main():
    while True:
        print("Checking for product availability...")
        for product in PRODUCTS:
            if check_stock(product):
                print(f"{product['name']} is available!")
                send_notification(product["name"])
                time.sleep(PAUSE_DURATION)
            else:
                print(f"{product['name']} is not available.")
        print("Waiting for the next check...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
