import os
from datetime import datetime 
from get_date import get_date
from format_time import format_time
from get_strategy import get_strategy
from get_pl import get_pl

TARGET_DIR = "src/trades"

def create_entry():

    ticker = input("Ticker: ").strip().upper()

    today = datetime.now().strftime("%Y-%m-%d")
    entry_date = get_date("Entry Date: ", default=today)
    entry_time = format_time(input("Entry Time: "))

    exit_date = get_date("Exit Date: ", default=entry_date, allow_empty=True)

    raw_exit_time = input("Exit Time: ")
    exit_time = format_time(raw_exit_time)

    strategy = get_strategy()

    direction = input("Direction: ")

    risk = input("Risk: ")

    pl = get_pl("P/L: ")

    # Make path and filename
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        
    # Replaces ':' with nothing ("") inside the time string
    filename = f"{ticker}-{entry_date}-{entry_time.replace(':', '')}.md".lower()

    filepath = os.path.join(TARGET_DIR, filename)

       # Inside the f-string, we use python logic: {value if value else 'null'}    
    content = f"""---
title: {ticker} {direction.capitalize()}
ticker: {ticker}
entryDate: {entry_date}
entryTime: {entry_time}
exitDate: {exit_date if exit_date else 'null'}
exitTime: {exit_time}
strategy: {strategy}
direction: {direction}
risk: {risk}
pl: {pl}
---

"""

    # Write the file
    try:
        with open(filepath, "w") as file:
            file.write(content)
        print(f"✅ Created: {filepath}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_entry()
