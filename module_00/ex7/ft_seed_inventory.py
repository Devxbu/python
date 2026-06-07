def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    sentence = ""
    seed_type = seed_type.capitalize()
    if unit == "packets":
        sentence = f"{seed_type} seeds: {quantity} packets available"
    elif unit == "grams":
        sentence = f"{seed_type} seeds: {quantity} grams total"
    elif unit == "area":
        sentence = f"{seed_type} seeds: covers {quantity} square meters"
    else:
        sentence = "Unknown unit type"
    print(sentence)
