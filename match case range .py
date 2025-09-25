def check_range(value):
    match value:
        case 0:
            print("Value is 0")
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case 3:
            print("Value is 3")
        case 4:
            print("Value is 4")
        case 5:
            print("Value is 5")
        case 6:
            print("Value is 6")
        case _:
            print("Value is out of range (0-6)")

# Example usage
check_range(3)
check_range(7)