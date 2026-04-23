import yaml

def calc_total_pl(file_path):
    total = 0.0
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            if isinstance(data, list):
                for entry in data:
                    total += float(entry.get('pl', 0))
        return total
    except Exception as e:
        print(f"Error reading trades: {e}")
        return None

# 1. Calculate the total from your YAML trades file
trades_file = 'src/data/trades.yml'
total_result = calc_total_pl(trades_file)

if total_result is not None:
    # 2. Write to a JS file instead of a YML file
    stats_file = 'src/data/tradestats.js'
    try:
        with open(stats_file, 'w') as f:
            # This writes a standard JS export line
            f.write(f"export const total_pl = {total_result};")
            
        print(f"Successfully updated {stats_file} with total: ${total_result:,.2f}")
    except Exception as e:
        print(f"Error writing JS file: {e}")
