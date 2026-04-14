def get_direction():
    raw_direction = input("Direction (l/s): ").strip().lower()

    # Convert shorthand to full words, otherwise capitalize the input
    direction = "Long" if raw_direction == "l" else "Short" if raw_direction == "s" else raw_direction.capitalize()

    # Optional: basic validation
    if direction not in ["Long", "Short"]:
        print(f"⚠️ Unexpected input '{direction}'. Defaulting to 'Long'.")
        direction = "Long"
        
    return direction
