import logging
import os

USE_MOCK = os.getenv("USE_MOCK", "False") == "True"

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # MOCK MODE
        if USE_MOCK:
            logging.info("Running in MOCK mode")

            order = {
                "orderId": 123456,
                "status": "FILLED",
                "executedQty": quantity,
                "avgPrice": price if price else "market_price"
            }

            logging.info(f"Mock Order: {order}")
            return order

        # REAL MODE
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                quantity=quantity,
                stopPrice=price
            )

        else:
            raise ValueError("Unsupported order type")

        logging.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Order Error: {str(e)}")
        raise