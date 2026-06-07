def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    sentence = ""
    if unit == "packets":
        sentence = f"{seed_type.capitalize()} seeds: {quantity} packets available"
    elif unit == "grams":
        sentence = f"{seed_type.capitalize()} seeds: {quantity} grams total"
    elif unit == "area":
        sentence = f"{seed_type.capitalize()} seeds: covers {quantity} square meters"
    else:
        sentence = "Unknown unit type"
    print(sentence)
