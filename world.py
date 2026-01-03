world = {
    1:{"up": 2, "down": 16, "right": 4},
    2:{"up": 3, "down": 1, "right": 15, "left":5},
    3:{"down": 2, "left":4},
    4:{"down": 6, "right": 3},
    5:{"down": 7, "right": 2},
    6:{"up": 4, "right": 7},
    7:{"up": 5, "down": 8, "right": 16, "left":6},
    8:{"up": 7, "right": 9},
    9:{"down": 11, "right": 10, "left":8},
    10:{"up": 14, "left":9},
    11:{"up": 9, "right": 12},
    12:{"up": 13, "left":11},
    13:{"down": 12,"left":14},
    14:{"up": 15, "down": 10, "right": 13, "left":1},
    15:{"down": 14, "left":2},
    16:{"up": 1, "left":7},
}

locationNames = {
    6: "Entrance",
    4: "Exit",
    3: "Checkout",
    12: "Produce",
    11: "Dairy",
    10: "Essentials",
    8: "Clothing",
    7: "Pharmacy",
    15: "Help Desk",
    2: "Returns",
    5: "Restaurant",
    13: "Bathroom"
}

storeItems = {
    # Produce
    12: {
        "Apple": 2,
        "Banana": 1,
        "Orange": 2,
        "Lettuce": 3,
        "Tomato": 2,
        "Potato": 1,
        "Grapes": 4
    },

    # Dairy
    11: {
        "Milk": 4,
        "Cheese": 5,
        "Yogurt": 3,
        "Butter": 4,
        "Eggs": 5,
        "Cream": 3
    },

    # Essentials
    10: {
        "Soap": 3,
        "Toothpaste": 4,
        "Shampoo": 6,
        "Conditioner": 6,
        "Toilet Paper": 8,
        "Paper Towels": 7,
        "Laundry Detergent": 10
    },

    # Clothing
    8: {
        "Shirt": 10,
        "Pants": 20,
        "Jacket": 35,
        "Socks": 5,
        "Shoes": 40,
        "Hat": 8
    },

    # Pharmacy
    7: {
        "Medicine": 8,
        "Bandages": 4,
        "Pain Reliever": 6,
        "Vitamins": 10,
        "Cough Syrup": 7,
        "Hand Sanitizer": 3
    },

    # Restaurant / Food Court
    5: {
        "Burger": 6,
        "Fries": 3,
        "Soda": 2,
        "Pizza Slice": 4,
        "Hot Dog": 4,
        "Ice Cream": 3
    }
}

playerLocation = 6
money = 100
cart = []
checkedOut = False

while (playerLocation != 4):
    print("\nYou are in the", locationNames.get(playerLocation, "Hallway"))
    print("You can go:")

    for direction, destination in world[playerLocation].items():
        destinationName = locationNames.get(destination, "Hallway")
        print(f"  {direction} → {destinationName}")



    movement = input("Enter direction (\"up\", \"down\", \"right\", \"left\")")
    if movement in world[playerLocation]:
        fromLocation = playerLocation
        toLocation = world[playerLocation][movement]

        if toLocation == 4 and checkedOut == False:
            print(f"\n\t\t\t\t\tGo to checkout otherwise leave items at exit")
        else:
            fromName = locationNames.get(fromLocation, "Hallway")
            toName = locationNames.get(toLocation, "Hallway")

            print(f"\n\t\t\t\t\tYou moved from {fromName} to {toName}")

            playerLocation = toLocation

        total = 0
        if playerLocation == 3 and checkedOut == False:
            for z in cart:
                for i in storeItems:
                    for j in storeItems[i]:
                        if j == z:
                            print(f"\n\t\t\t\t\t{j}: ${storeItems[i][j]}")
                            total += storeItems[i][j]
            print(f"\n\t\t\t\t\tCart Total: ${total}")

            money -= total
            checkedOut = True

    else:
        print("Sorry, please choose a different direction")

    print()

    if playerLocation in storeItems:
        print("Items for sale:")
        for item, price in storeItems[playerLocation].items():
            print(item, "- $", price)

        choice = input("Type item name to add to cart or 'skip': ")

        while(choice != 'skip'):
            if choice in storeItems[playerLocation]:
                cart.append(choice)
                print(choice, "added to cart")
            choice = input("Type item name to add to cart or 'skip': ")

print("thank you for coming")