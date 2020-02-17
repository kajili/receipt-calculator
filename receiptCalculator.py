# peopleList = ["Joe", "Tylenol", "Dilbo", "Satan", "Bill Cosby"] # Test peopleList
peopleList = ["Kevin", "Christian", "Payvand", "Conner", "Bridget", "Nolan"]

items = [
    # [item[0] = itemTotal, item[1] = itemPrice, item[2] = peopleList, item[3] = purchasedBy / payToThisPerson]

    # Test Data
    # ["Tomato", 5,
    #     ["Joe", "Tylenol", "Dilbo", "Bill Cosby"],
    #     "Bill Cosby"
    # ],
    # ["Chicken", 20,
    #     ["Joe", "Tylenol", "Satan", "Dilbo", "Bill Cosby"],
    #     "Bill Cosby"
    # ],
    # ["Beef", 30,
    #     ["Tylenol", "Dilbo", "Bill Cosby"],
    #     "Tylenol"
    # ],
    # ["Rum", 30,
    #     ["Tylenol", "Joe", "Satan", "Dilbo"],
    #     "Joe"
    # ]

    ["805 Firestone Ale", 27.19, 
        ["Conner", "Nolan", ],
        "Ianey"
    ],

    ["Modelo", 24.16, 
        ["Christian", "Conner", ],
        "Ianey"
    ],

    ["Gatorade Fierce", 18, 
        ["Christian", "Payvand", "Conner", "Nolan", ],
        "Ianey"
    ],

    ["Kirkland Scotch", 17.99,
        [],
        "Ianey"
    ],

    ["Sourdough", 4.89,
        ["Christian", "Payvand", "Conner", "Nolan", ],
        "Ianey"
    ],

    ["Kirkland PB Pretzel", 8.49,
        ["Christian", "Payvand", "Conner", "Nolan", "Bridget", ],
        "Ianey"
    ],

    ["Kirkland Chicken Tenderloins", 15.99,
        ["Kevin", "Christian", "Payvand", "Nolan", ],
        "Ianey"
    ],

    ["Mini Peppers", (4.49 * 2),
        ["Kevin", "Christian", "Payvand", "Bridget", ],
        "Ianey"
    ],
    
    ["Ground Beef", 16.48,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", ],
        "Ianey"
    ],
    
    ["Steak Flap Meat", 16.77,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", ],
        "Ianey"
    ],

    ["Corn Tortillas", 3.19,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", ],
        "Ianey"
    ],

    ["Chocolate Chip Cookie Dough", 6.99,
        ["Christian", "Payvand", "Conner", "Nolan", ],
        "Ianey"
    ],
    
    ["Kirkland Mex Cheese", 13.79,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", ],
        "Ianey"
    ],
            
    ["Kirkland Eggs", (3.79 * 2),
        ["Christian", "Payvand", "Conner", "Nolan"],
        "Ianey"
    ],

    ["Vine Tomatoes", 5.29,
        ["Kevin", "Christian", "Payvand", "Bridget"],
        "Ianey"
    ],
            
    ["Kirkland Chicken Thighs", 15.48,
        ["Kevin", "Christian", "Payvand", "Nolan", "Bridget"],
        "Ianey"
    ],

    ["Broccoli", 4.99,
        ["Christian", "Payvand", ],
        "Ianey"
    ],
            
    ["Costco Combo Salsa", 5.79,
        ["Kevin", "Christian", "Payvand", "Bridget"],
        "Ianey"
    ],
            
    ["Elysian IPA", 22.59,
        ["Payvand", "Conner", ],
        "Ianey"
    ],
            
    ["Floridas Orange Juice", (3.49 * 2),
        ["Christian", ],
        "Ianey"
    ],
            
    ["SB Mozzarella", 6.99,
        ["Kevin", "Christian", "Payvand", "Conner", ],
        "Ianey"
    ],
            
    ["SB Tonic Water", (1.10 * 2),
        [],
        "Ianey"
    ],
            
    ["SB Drinking Water", (0.99 * 4),
        ["Kevin", "Christian", "Payvand", "Nolan", "Bridget"],
        "Ianey"
    ],
            
    ["Coca-Cola Classic", (1.77 * 3),
        ["Payvand", "Conner", ],
        "Ianey"
    ],
            
    ["Classico Alfredo Sauce", 2.99,
        ["Kevin", "Christian", "Conner", ],
        "Ianey"
    ],
            
    ["Classico Red Sauce", 2.99,
        ["Christian", "Payvand", ],
        "Ianey"
    ],
            
    ["Barilla Gluten Free Lasagne", 2.99,
        ["Kevin", "Christian", "Conner", ],
        "Ianey"
    ],
            
    ["SB Lasagne", 1.69,
        ["Christian", "Payvand", ],
        "Ianey"
    ],
            
    ["Hormel Spam", (2.99 * 2),
        ["Christian", ],
        "Ianey"
    ],
            
    ["Salad Spinach", (1.99 * 2),
        ["Christian", "Payvand", "Bridget"],
        "Ianey"
    ],

    ["Drinking Water", (3.99 * 2),
        ["Kevin", "Christian", "Bridget", "Nolan", ],
        "Kevin"
    ],
            
    ["Lactaid Milk", 2.99,
        ["Bridget", "Nolan", ],
        "Nolan"
    ],
            
    ["Jumex Nectar", (1.29 * 3),
        ["Payvand", "Conner", "Nolan", ],
        "Nolan"
    ],
            
    ["SB Marshmallows", 1.25,
        ["Payvand", "Conner", "Nolan", "Bridget"],
        "Nolan"
    ],
            
    ["Swiss Miss Cocao", 6.99,
        ["Payvand", "Nolan", "Bridget"],
        "Nolan"
    ],
                
    ["Sour Cream", 2.49,
        ["Kevin", "Nolan", "Bridget"],
        "Payvand"
    ],
                
    ["Tostitos Salsa", 5.29,
        ["Kevin", "Christian", "Payvand", ],
        "Payvand"
    ],
                
    ["Tostitos Chips", 2.99,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget"],
        "Payvand"
    ],

    ["Vodka", 30,
        ["Kevin", "Christian", "Conner", "Nolan"],
        "Conner"
    ]
            
    
]


def receiptCalculator(itemList):

    result = []

    for person in peopleList:
        totalPricePerPerson = 0
        payAmountTo = {}
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

                if(item[3] in payAmountTo):
                    payAmountTo[item[3]] += itemPricePerPerson
                else:
                    payAmountTo[item[3]] = itemPricePerPerson

                totalPricePerPerson += itemPricePerPerson

        result.append("\n")
        
        for paidPerson in payAmountTo:
            if(person != paidPerson):
                result.append(
                "   Price to PAY TO "
                + paidPerson
                + ": $"
                + str("{0:.2f}".format(payAmountTo[paidPerson]))

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

