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

## Notes
- Orders may remain in `NEW` state due to Binance testnet simulated execution.
- Minimum notional value ($100) is required for orders.
- Price filters apply for LIMIT orders.

## Supported Commands

| Order Type  | Description                                |
|-------------|--------------------------------------------|
| MARKET      | Instant execution                          |
| LIMIT       | Price-controlled order                     |
| STOP_MARKET | Trigger-based order (stop loss / breakout) |

## Notes
- Orders may remain in `NEW` state due to Binance testnet.
- STOP orders may return partial response.
- Minimum notional ($100) required.

## Example Commands

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

## Features
- CLI-based trading bot
- Binance Futures Testnet integration
- Market, Limit, and Stop-Market orders
- Input validation
- Logging system
- Error handling

## Verification
Orders verified using:
- CLI output
- Log files
- Binance testnet UI