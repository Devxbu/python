def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for d in range(1, days + 1):
        print(f"Day {d}")
    print("Harvest time!")
