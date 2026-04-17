def get_instrument_type():

  types = [
        "Forex",
        "Option"
    ]
    
  print("\n--- Select Intrument Type ---")
  for i, s in enumerate(types, 1):
      print(f"{i}. {s}")
      
  user_input = input("Type (#): ").strip()

  # 1. Check if user picked a number from the list
  if user_input.isdigit():
      choice = int(user_input)
      if 1 <= choice <= len(types):
          return types[choice - 1]
  
  # 2. If it's a new name, capitalize every word (e.g., "power trend" -> "Power Trend")
  if user_input:
      return user_input.title()

  # 3. Fallback
  print("⚠️ No input detected. Defaulting to 'Discretionary'.")
  return "Discretionary"
