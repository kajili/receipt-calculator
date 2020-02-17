peopleList = ["Joe", "Tylenol", "Dilbo", "Satan", "Bill Cosby"] # Test peopleList
# peopleList = ["Kevin", "Christian", "Payvand"]

items = [
    # [item[0] = itemTotal, item[1] = itemPrice, item[2] = peopleList, item[3] = purchasedBy / payToThisPerson]

    # Test Data
    ["Tomato", 5,
        ["Joe", "Tylenol", "Dilbo", "Bill Cosby"],
        "Bill Cosby"
    ],
    ["Chicken", 20,
        ["Joe", "Tylenol", "Satan", "Dilbo", "Bill Cosby"],
        "Bill Cosby"
    ],
    ["Beef", 30,
        ["Tylenol", "Dilbo", "Bill Cosby"],
        "Tylenol"
    ],
    ["Rum", 30,
        ["Tylenol", "Joe", "Satan", "Dilbo"],
        "Joe"
    ]

    # ["Firestone Ale", 27.19, 
    #     []],

    # ["Modelo", 24.16, 
    #     ["Christian", ]],

    # ["Gatorade Fierce", 18, 
    #     ["Christian", "Payvand"]],

    # ["Kirkland Scotch", 17.99,
    #     []],

    # ["Sourdough", 4.89,
    #     ["Christian", "Payvand"]],

    # ["Kirkland PB Pretzel", 8.49,
    #     ["Christian", "Payvand"]],

    # ["Kirkland Chicken", 15.99,
    #     ["Kevin", "Christian", "Payvand"]],

    # ["Mini Peppers", (4.49 * 2),
    #     ["Kevin", "Christian", "Payvand"]],
    
    # ["Ground Beef", 16.48,
    #     ["Kevin", "Christian", "Payvand"]],
    
    # ["Steak Flap Meat", 16.77,
    #     ["Kevin", "Christian", "Payvand"]],

    # ["Corn Tortillas", 3.19,
    #     ["Kevin", "Christian", "Payvand"]],

    # ["Chocolate Chip Cookie Dough", 6.99,
    #     ["Christian", "Payvand", ]],
    
    # ["Kirkland Mex Cheese", 13.79,
    #     ["Kevin", "Christian", "Payvand", ]],
            
    # ["Kirkland Eggs", (3.79 * 2),
    #     ["Christian", "Payvand", ]],

    # ["Vine Tomatoes", 5.29,
    #     ["Kevin", "Christian", "Payvand", ]],
            
    # ["Kirkland Chicken Thighs", 15.48,
    #     ["Kevin", "Christian", "Payvand", ]],

    # ["Broccoli", 4.99,
    #     ["Christian", "Payvand", ]],
            
    # ["Costco Combo Salsa", 5.79,
    #     ["Kevin", "Christian", "Payvand",]],
            
    # ["Elysian IPA", 22.59,
    #     ["Payvand", ]],
            
    # ["Floridas Orange Juice", (3.49 * 2),
    #     ["Christian", ]],
            
    # ["SB Mozzarella", 6.99,
    #     ["Kevin", "Christian", "Payvand", ]],
            
    # ["SB Tonic Water", (1.10 * 2),
    #     []],
            
    # ["SB Drinking Water", (0.99 * 4),
    #     ["Kevin", "Christian", "Payvand", ]],
    
    # ["Drinking Water", (3.99 * 2),
    #     ["Kevin", "Christian", ]],
            
    # ["Coca-Cola Classic", (1.77 * 3),
    #     ["Payvand", ]],
            
    # ["Classico Alfredo Sauce", 2.99,
    #     ["Kevin", "Christian", ]],
            
    # ["Classico Red Sauce", 2.99,
    #     ["Christian", "Payvand", ]],
            
    # ["Barilla Gluten Free Lasagne", 2.99,
    #     ["Kevin", "Christian", ]],
            
    # ["SB Lasagne", 1.69,
    #     ["Christian", "Payvand", ]],
            
    # ["Hormel Spam", (2.99 * 2),
    #     ["Christian", ]],
            
    # ["Salad Spinach", (1.99 * 2),
    #     ["Christian", "Payvand", ]],
            
    # ["Lactaid Milk", 2.99,
    #     []],
            
    # ["Jumex Nectar", (1.29 * 3),
    #     ["Payvand", ]
    #     "Nolan"],
            
    # ["SB Marshmallows", 1.25,
    #     ["Payvand", ]],
            
    # ["Swiss Miss Cocao", 6.99,
    #     ["Payvand", ]],
                
    # ["Sour Cream", 2.49,
    #     ["Kevin", ]],
                
    # ["Tostitos Salsa", 5.29,
    #     ["Kevin", "Christian", "Payvand", ]],
                
    # ["Tostitos Chips", 2.99,
    #     ["Kevin", "Christian", "Payvand", ]]
            
    
]


def receiptCalculator(itemList):

    result = []

    for person in peopleList:
        totalPricePerPerson = 0
        payAmountTo = []
        result.append(person + " pays:\n")
        for item in itemList:
            if person in item[2]:
                itemPricePerPerson = item[1] / len(item[2])
                result.append(
                    "     $"
                    + str("{0:.2f}".format(itemPricePerPerson))
                    + " for "
                    + item[0]
                    + " paid to: "
                    + item[3]
                )
                payAmountTo.append([item[3], itemPricePerPerson])
                totalPricePerPerson += itemPricePerPerson

        result.append("\n")
        
        for paidPerson in payAmountTo:
            if(person != paidPerson[0]):
                result.append(
                "   Price to PAY TO "
                + paidPerson[0]
                + ": $"
                + str("{0:.2f}".format(paidPerson[1]))

                )

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

