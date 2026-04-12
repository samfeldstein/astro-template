def get_date(prompt, default=None, allow_empty=False):
    """
    Loops until valid date. 
    If 'default' is provided, hitting Enter returns that value silently.
    """
    # ❌ Removed the visual prompt modification here
    
    while True:
        raw = input(prompt).strip()
        
        # 1. Handle Enter Key
        if raw == "":
            if default:
                return default  # Hidden feature: Auto-fills default
            if allow_empty:
                return ""       # Returns blank
        
        formatted = raw

        # 2. Auto-Format
        if len(raw) == 8 and raw.isdigit():
            formatted = f"{raw[:4]}-{raw[4:6]}-{raw[6:]}"
        
        # 3. Validation
        if len(formatted) == 10:
            return formatted
            
        print(f"❌ Invalid format: '{raw}'. Please use YYYY-MM-DD.")
