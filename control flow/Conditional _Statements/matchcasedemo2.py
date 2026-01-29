month = int(input("enter a  month num : "))

match month:
    case 1:
        print("jan")
    case 2:
        print("feb")
    case 3:
        print("mar")
    case _:
        print("invalid month")
