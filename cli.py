import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)
    parser.add_argument("--stop_price", required=False)

    args = parser.parse_args()

    try:
        # Combine price and stop_price
        price_input = args.price if args.price else args.stop_price

        symbol, side, order_type, quantity, price = validate_input(
            args.symbol, args.side, args.type, args.quantity, price_input
        )

        client = get_client()

        print("\n📊 Order Request Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            if order_type == "STOP_MARKET":
                print(f"Stop Price: {price}")
            else:
                print(f"Price: {price}")

        order = place_order(client, symbol, side, order_type, quantity, price)

        print("\n✅ Order Response")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n❌ Error:", str(e))


if __name__ == "__main__":
    main()