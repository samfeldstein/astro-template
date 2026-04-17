import os
from datetime import datetime 
from get_date import get_date
from format_time import format_time
from get_strategy import get_strategy
from get_pl import get_pl
from get_direction import get_direction
from get_ticker import get_ticker
from get_instrument_type import get_instrument_type

DATA_FILE = "src/data/trades.yml"

def create_entry():
    ticker = get_ticker()
    instrument = get_instrument_type()
    today = datetime.now().strftime("%Y-%m-%d")
    entry_date = get_date("Entry Date: ", default=today)
    entry_time = format_time(input("Entry Time: "))
    exit_date = get_date("Exit Date: ", default=entry_date, allow_empty=True)
    exit_time = format_time(input("Exit Time: "))
    strategy = get_strategy()
    direction = get_direction()
    risk = input("Risk: ")
    pl = get_pl("P/L: ")
    id = f"{ticker}-{entry_date}-{entry_time.replace(':', '')}".lower()

    entry = f"""
- id: {id}
  title: {ticker} {direction.capitalize()}
  ticker: {ticker}
  instrument: {instrument}
  entryDate: {entry_date}
  entryTime: {entry_time}
  exitDate: {exit_date if exit_date else 'null'}
  exitTime: {exit_time}
  strategy: {strategy}
  direction: {direction}
  risk: {risk}
  pl: {pl}
  notes: |
"""

    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "a") as file:
            file.write(entry)
        print(f"✅ Entry added to {DATA_FILE}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_entry()