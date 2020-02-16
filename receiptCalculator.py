peopleList = ["name", "test"]

items = [
    # [item[0] = itemName, item[1] = itemPrice, item[2] = peopleList]
    # ["Tomato", 5,
    #     ["Joe", "Tylenol", "Dilbo", "Bill Cosby"]],
    # ["Chicken", 20,
    #     ["Joe", "Tylenol", "Satan", "Dilbo", "Bill Cosby"]],
    # ["Beef", 30,
    #     ["Tylenol", "Dilbo", "Bill Cosby"]],
    # ["Rum", 30,
    #     ["Tylenol", "Joe", "Satan", "Dilbo"]]

    ["Firestone Ale", 27.19, 
        ["name", ]],

    ["Modelo", 24.16, 
        ["name", ]],

    ["Gatorade Fierce", 18, 
        ["name", ]],

    ["Kirkland Scotch", 17.99,
        ["name", ]],

    ["Sourdough", 4.89,
        ["name", ]],

    ["Kirkland PB Pretzel", 8.49,
        ["name", ]],

    ["Kirkland Chicken", 15.99,
        ["name", ]],

    ["Mini Peppers", 4.49,
        ["name", ]],
    
    # ["Ground", 4,
    #     ["name", ]],
    
    # ["item", 4,
    #     ["name", ]],

    # ["item", 4,
    #     ["name", ]],

    # ["item", 4,
    #     ["name", ]],
    
    # ["item", 4,
    #     ["name", ]],
    
    # ["item", 4,
    #     ["name", ]],
            
    # ["item", 4,
    #     ["name", ]],
            
    # ["item", 4,
    #     ["name", ]],
            
    # ["item", 4,
    #     ["name", ]],
    
]


def receiptCalculator(itemList):

    result = []

    for person in peopleList:
        totalPricePerPerson = 0
        result.append(person + " pays:\n")
        for item in itemList:
            if person in item[2]:
                itemPricePerPerson = item[1] / len(item[2])
                result.append(
                    "     $"
                    + str("{0:.2f}".format(itemPricePerPerson))
                    + " for "
                    + item[0]
                )
                totalPricePerPerson += itemPricePerPerson
        result.append(
            "\n   Total Price for "
            + person
            + ": $"
            + str("{0:.2f}".format(totalPricePerPerson))
        )
        result.append("\n")
    return result


priceList = receiptCalculator(items)

for price in priceList:
    print(price)

