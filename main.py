import requests
import telegram
import time
import datetime

# CoinMarketCap API URL
url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

# Telegram Bot Token and Chat ID
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

# Create a Telegram bot object
bot = telegram.Bot(token=bot_token)

# Function to get the top 10 cryptocurrency market capitalizations
def get_market_cap():
    response = requests.get(url).json()
    market_caps = [coin["name"] + ": $" + coin["market_cap_usd"] for coin in response]
    return "\n".join(market_caps)

# Function to send a message to Telegram chat
def send_message(text):
    bot.send_message(chat_id=chat_id, text=text)

