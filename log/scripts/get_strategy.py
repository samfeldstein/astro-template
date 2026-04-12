# input_strategy.py

def get_strategy():
    strategies = [
        "superzone"
    ]
    
    print("\n--- Select Strategy ---")
    for i, s in enumerate(strategies, 1):
        print(f"{i}. {s}")
        
    try:
        choice = int(input("Strategy (#): "))
        return strategies[choice - 1]
    except (ValueError, IndexError):
        print("⚠️ Invalid selection. Defaulting to 'Discretionary'.")
        return "Discretionary"

# Make sure NO code exists below this function at the indentation level 0
