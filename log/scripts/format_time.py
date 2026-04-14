def format_time(raw_time):
    # Ensure it's a string and strip whitespace
    clean = str(raw_time).strip()
    
    # Pad with zeros until it's 4 characters long (e.g., "18" -> "0018")
    clean = clean.zfill(4)
    
    # Insert the colon
    return f"{clean[:2]}:{clean[2:]}"

