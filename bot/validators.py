def validate_input(symbol, side, order_type, quantity, price):
    side = side.upper()
    order_type = order_type.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_MARKET")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except:
        raise ValueError("Quantity must be a positive number")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")

    if order_type == "STOP_MARKET":
        if price is None:
            raise ValueError("Stop price required for STOP_MARKET")

    return symbol.upper(), side, order_type, quantity, price