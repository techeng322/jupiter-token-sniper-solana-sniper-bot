import requests

# Authentication credentials (replace with your actual credentials)
API_KEY = 'your_api_key'

# Base URL for Jupiter V6 API
BASE_URL = 'https://jupiterv6api.com'

# Function to buy tokens
def buy_tokens(symbol, amount, price):
    """Send a buy order for tokens using the Jupiter V6 API."""
    url = f'{BASE_URL}/buy'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {'symbol': symbol, 'amount': amount, 'price': price}

    # Send POST request to buy tokens
    response = requests.post(url, headers=headers, json=data)

    # Handle response
    if response.status_code == 200:
        print('Buy order successful!')
    else:
        print('Buy order failed. Error:', response.text)

# Function to sell tokens
def sell_tokens(symbol, amount, price):
    """Send a sell order for tokens using the Jupiter V6 API."""
    url = f'{BASE_URL}/sell'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {'symbol': symbol, 'amount': amount, 'price': price}

    # Send POST request to sell tokens
    response = requests.post(url, headers=headers, json=data)

    # Handle response
    if response.status_code == 200:
        print('Sell order successful!')
    else:
        print('Sell order failed. Error:', response.text)

# Example usage
if __name__ == "__main__":
    # Example buy order
    buy_tokens('SOL', 10, 50)  # Buy 10 SOL at a price of 50 USD each
    
    # Example sell order
    sell_tokens('SOL', 5, 60)  # Sell 5 SOL at a price of 60 USD each