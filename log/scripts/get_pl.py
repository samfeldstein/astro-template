def get_pl(prompt):
    """
    Accepts input like "423.5", "100", or "-50".
    Returns formatted string: "423.50", "100.00", "-50.00".
    """
    while True:
        # 1. Get input and remove '$' if user typed it
        raw = input(prompt).strip().replace('$', '')
        
        try:
            # 2. Convert to float to validate it is a number
            value = float(raw)
            
            # 3. Format to strictly 2 decimal places
            return f"{value:.2f}"
            
        except ValueError:
            print("❌ Invalid amount. Please enter a number (e.g., 423.50).")
