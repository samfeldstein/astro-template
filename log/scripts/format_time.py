def format_time(raw_time):
    """
    Takes raw time string (846, 0846, 1430).
    Returns formatted string: 08:46.
    """
    clean = raw_time.strip()
    
    # 1. Auto-Pad: Turn "846" into "0846"
    if len(clean) == 3 and clean.isdigit():
        clean = "0" + clean
        
    # 2. Format: Turn "0846" into "08:46"
    if len(clean) == 4 and clean.isdigit():
        return f"{clean[:2]}:{clean[2:]}"
        
    return clean