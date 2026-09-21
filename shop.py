def open_shop():
    print("welcom to the shop!")
    print("1. ostaa miekan: 14 euroa")
    print("2. ostaa tacki: 140 euroa")

    choice= input("mistä haluat ostamaan?")
    if (choice== "1"):
        print("sinä ostat miekan")
        return "miekan"
    elif (choice=="2"):
        print("sinä ostat tacki")
        return "taki"
    else:
        print("et valitse mitään")
        return None
#commment2