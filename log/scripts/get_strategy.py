def get_strategy():
    strategies = [
        "Superzone",
        "Alone97"
    ]
    
    print("\n--- Select Strategy ---")
    for i, s in enumerate(strategies, 1):
        print(f"{i}. {s}")
    print("Or type a new strategy name.")
        
    user_input = input("Strategy (# or Name): ").strip()

    # 1. Check if user picked a number from the list
    if user_input.isdigit():
        choice = int(user_input)
        if 1 <= choice <= len(strategies):
            return strategies[choice - 1]
    
    # 2. If it's a new name, capitalize every word (e.g., "power trend" -> "Power Trend")
    if user_input:
        return user_input.title()

    # 3. Fallback
    print("⚠️ No input detected. Defaulting to 'Discretionary'.")
    return "Discretionary"
