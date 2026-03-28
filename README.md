# Binance Futures Testnet Trading Bot

## Features
- Market & Limit order support
- BUY / SELL support
- CLI interface
- Input validation
- Logging (trading.log)
- Error handling
- Mock mode support

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Add API keys in `.env`

3. Run examples:

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Logs
All API activity is logged in `trading.log`

## Assumptions
- Uses Binance Futures Testnet
- Quantity and price formats are valid

## Note
If API is unavailable, set:
USE_MOCK=True