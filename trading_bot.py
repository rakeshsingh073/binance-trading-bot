
import logging
from binance.client import Client
from binance.enums import *

# Logging configuration
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        # Use Binance Futures Testnet
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'  
        logging.info("Bot initialized with testnet: %s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_config = {
                'symbol': symbol,
                'side': SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                'type': order_type,
                'quantity': quantity
            }

            if order_type == ORDER_TYPE_LIMIT:
                order_config['price'] = price
                order_config['timeInForce'] = TIME_IN_FORCE_GTC

            result = self.client.futures_create_order(**order_config)
            logging.info("Order placed: %s", result)
            return result
        except Exception as e:
            logging.error("Failed to place order: %s", e)
            return None
