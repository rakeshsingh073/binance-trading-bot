from trading_bot import BasicBot

def get_user_input():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Buy or Sell: ").lower()
    order_type = input("Order Type (MARKET or LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == 'LIMIT':
        price = float(input("Enter Limit Price: "))

    return symbol, side, order_type, quantity, price

if __name__ == "__main__":
    print("=== Binance Futures Testnet Trading Bot ===")

    api_key = input("Enter your Binance API Key: ")
    api_secret = input("Enter your Binance API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        try:
            symbol, side, order_type, quantity, price = get_user_input()
            response = bot.place_order(symbol, side, order_type, quantity, price)
            if response:
                print("✅ Order placed successfully!")
                print(response)
            else:
                print("❌ Failed to place order.")
        except Exception as err:
            print("⚠️ Error:", err)

        again = input("Place another order? (y/n): ")
        if again.lower() != 'y':
            break
