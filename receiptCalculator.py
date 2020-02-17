peopleList = ["Total", "Kevin"]

items = [
    # [item[0] = itemTotal, item[1] = itemPrice, item[2] = peopleList]

    # ["Tomato", 5,
    #     ["Joe", "Tylenol", "Dilbo", "Bill Cosby"]],
    # ["Chicken", 20,
    #     ["Joe", "Tylenol", "Satan", "Dilbo", "Bill Cosby"]],
    # ["Beef", 30,
    #     ["Tylenol", "Dilbo", "Bill Cosby"]],
    # ["Rum", 30,
    #     ["Tylenol", "Joe", "Satan", "Dilbo"]]

    ["Firestone Ale", 27.19, 
        ["Total", ]],

    ["Modelo", 24.16, 
        ["Total", ]],

    ["Gatorade Fierce", 18, 
        ["Total", ]],

    ["Kirkland Scotch", 17.99,
        ["Total", ]],

    ["Sourdough", 4.89,
        ["Total", ]],

    ["Kirkland PB Pretzel", 8.49,
        ["Total", ]],

    ["Kirkland Chicken", 15.99,
        ["Total", "Kevin", ]],

    ["Mini Peppers", (4.49 * 2),
        ["Total", "Kevin", ]],
    
    ["Ground Beef", 16.48,
        ["Total", "Kevin", ]],
    
    ["Steak Flap Meat", 16.77,
        ["Total", "Kevin", ]],

    ["Corn Tortillas", 3.19,
        ["Total", "Kevin", ]],

    ["Chocolate Chip Cookie Dough", 6.99,
        ["Total", ]],
    
    ["Kirkland Mex Cheese", 13.79,
        ["Total", "Kevin", ]],
            
    ["Kirkland Eggs", (3.79 * 2),
        ["Total", ]],

    ["Vine Tomatoes", 5.29,
        ["Total", "Kevin", ]],
            
    ["Kirkland Chicken Thighs", 15.48,
        ["Total", "Kevin", ]],

    ["Broccoli", 4.99,
        ["Total", ]],
            
    ["Combo Salsa", 5/79,
        ["Total", "Kevin", ]],
            
    ["Elysian IPA", 22.59,
        ["Total", ]],
            
    ["Floridas Orange Juice", (3.49 * 2),
        ["Total", ]],
            
    ["SB Mozzarella", 6.99,
        ["Total", "Kevin", ]],
            
    ["SB Tonic Water", (1.10 * 2),
        ["Total", ]],
            
    ["SB Drinking Water", (0.99 * 4),
        ["Total", "Kevin", ]],
            
    ["Coca-Cola Classic", (1.77 * 3),
        ["Total", ]],
            
    ["Classico Alfredo Sauce", 2.99,
        ["Total", "Kevin", ]],
            
    ["Classico Red Sauce", 2.99,
        ["Total", ]],
            
    ["Barilla Gluten Free Lasagne", 2.99,
        ["Total", "Kevin", ]],
            
    ["SB Lasagne", 1.69,
        ["Total", ]],
            
    ["Hormel Spam", (2.99 * 2),
        ["Total", ]],
            
    ["Salad Spinach", (1.99 * 2),
        ["Total", ]],
            
    ["Lactaid Milk", 2.99,
        ["Total", ]],
            
    ["Jumex Nectar", (1.29 * 3),
        ["Total", ]],
            
    ["SB Marshmallows", 1.25,
        ["Total", ]],
            
    ["Swiss Miss Cocao", 6.99,
        ["Total", ]],
                
    ["Sour Cream", 2.49,
        ["Total", "Kevin", ]],
                
    ["Tostitos Salsa", 5.29,
        ["Total", "Kevin", ]],
                
    ["Tostitos Chips", 2.99,
        ["Total", "Kevin", ]]
            
    
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

