def helper(days, current_day=1):
    if days > 0:
        print(f"Day {current_day}")
        helper(days - 1, current_day + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(days)
    print("Harvest time!")
