def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    sentence = ""
    if unit == "packets":
        sentence = f"{seed_type.capitalize()}: {quantity} packets available"
    elif unit == "grams":
        sentence = f"{seed_type.capitalize()}: {quantity} grams total"
    elif unit == "area":
        sentence = f"{seed_type.capitalize()}: covers {quantity} square meters"
    else:
        sentence = "Unknown unit type"
    print(sentence)
