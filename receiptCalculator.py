# peopleList = ["Joe", "Tylenol", "Dilbo", "Satan", "Bill Cosby"] # Test peopleList
peopleList = ["Kevin", "Christian", "Payvand", "Conner", "Bridget", "Nolan", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"]

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
        ["Conner", "Nolan", "Ianey", "Michael", "Ivan", ],
        "Ianey"
    ],

    ["Modelo", 24.16, 
        ["Christian", "Conner", "Hannah", "Ianey", "Michael", "Ivan"],
        "Ianey"
    ],

    ["Gatorade Fierce", 18, 
        ["Christian", "Payvand", "Conner", "Nolan", "Hannah", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],

    ["Kirkland Scotch", 17.99,
        ["Ianey", "Ianey", "Michael", "Ivan"],
        "Ianey"
    ],

    ["Sourdough", 4.89,
        ["Christian", "Payvand", "Conner", "Nolan", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],

    ["Kirkland PB Pretzel", 8.49,
        ["Christian", "Payvand", "Conner", "Nolan", "Bridget", "Hannah", ],
        "Ianey"
    ],

    ["Kirkland Chicken Tenderloins", 15.99,
        ["Kevin", "Christian", "Payvand", "Nolan", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],

    ["Mini Peppers", (4.49 * 2),
        ["Kevin", "Christian", "Payvand", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Ivan"],
        "Ianey"
    ],
    
    ["Ground Beef", 16.48,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Hannah", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
    
    ["Steak Flap Meat", 16.77,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Chris"],
        "Ianey"
    ],

    ["Corn Tortillas", 3.19,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],

    ["Chocolate Chip Cookie Dough", 6.99,
        ["Christian", "Payvand", "Conner", "Nolan", "Hannah", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
    
    ["Kirkland Mex Cheese", 13.79,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
            
    ["Kirkland Eggs", (3.79 * 2),
        ["Christian", "Payvand", "Conner", "Nolan", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],

    ["Vine Tomatoes", 5.29,
        ["Kevin", "Christian", "Payvand", "Bridget", "Hannah", "Steph", "Ianey", "Michael",],
        "Ianey"
    ],
            
    ["Kirkland Chicken Thighs", 15.48,
        ["Kevin", "Christian", "Payvand", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],

    ["Broccoli", 4.99,
        ["Christian", "Payvand", "Ianey", "Michael",],
        "Ianey"
    ],
            
    ["Costco Combo Salsa", 5.79,
        ["Kevin", "Christian", "Payvand", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Ivan", ],
        "Ianey"
    ],
            
    ["Elysian IPA", 22.59,
        ["Payvand", "Conner", "Ianey", "Michael", "Ivan",],
        "Ianey"
    ],
            
    ["Floridas Orange Juice", (3.49 * 2),
        ["Christian", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
            
    ["SB Mozzarella", 6.99,
        ["Kevin", "Christian", "Payvand", "Conner", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
            
    ["SB Tonic Water", (1.10 * 2),
        ["Ianey", "Michael",],
        "Ianey"
    ],
            
    ["SB Drinking Water", (0.99 * 4),
        ["Kevin", "Christian", "Payvand", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Chris", "Ivan"],
        "Ianey"
    ],
            
    ["Coca-Cola Classic", (1.77 * 3),
        ["Payvand", "Conner", "Hannah", ],
        "Ianey"
    ],
            
    ["Classico Alfredo Sauce", 2.99,
        ["Kevin", "Christian", "Conner", "Hannah", "Steph", "Ianey", "Michael", ],
        "Ianey"
    ],
            
    ["Classico Red Sauce", 2.99,
        ["Christian", "Payvand", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
            
    ["Barilla Gluten Free Lasagne", 2.99,
        ["Kevin", "Christian", "Conner", "Hannah", "Steph", "Ianey", "Michael",],
        "Ianey"
    ],
            
    ["SB Lasagne", 1.69,
        ["Christian", "Payvand", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Ianey"
    ],
            
    ["Hormel Spam", (2.99 * 2),
        ["Christian", "Ianey", "Michael", ],
        "Ianey"
    ],
            
    ["Salad Spinach", (1.99 * 2),
        ["Christian", "Payvand", "Bridget", "Hannah", "Steph", "Ianey", "Michael",],
        "Ianey"
    ],

    ["Drinking Water", (3.99 * 2),
        ["Kevin", "Christian", "Payvand", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", "Chris", "Ivan"],
        "Kevin"
    ],
            
    ["Lactaid Milk", 2.99,
        ["Bridget", "Nolan", ],
        "Nolan"
    ],
            
    ["Jumex Nectar", (1.29 * 3),
        ["Payvand", "Conner", "Nolan", "Ivan", "Ianey", "Michael"],
        "Nolan"
    ],
            
    ["SB Marshmallows", 1.25,
        ["Payvand", "Conner", "Nolan", "Bridget", "Hannah", "Ianey", "Michael", "Ivan", "Chris"],
        "Nolan"
    ],
            
    ["Swiss Miss Cocao", 6.99,
        ["Payvand", "Nolan", "Bridget", "Hannah", ],
        "Nolan"
    ],
                
    ["Sour Cream", 2.49,
        ["Kevin", "Nolan", "Bridget", "Hannah", "Steph", "Ianey", "Michael", ],
        "Payvand"
    ],
                
    ["Tostitos Salsa", 5.29,
        ["Kevin", "Christian", "Payvand", "Ianey", "Michael", ],
        "Payvand"
    ],
                
    ["Tostitos Chips", 2.99,
        ["Kevin", "Christian", "Payvand", "Conner", "Nolan", "Bridget", "Hannah", "Ianey", "Michael", ],
        "Payvand"
    ],

    ["Vodka", 30,
        ["Kevin", "Christian", "Conner", "Nolan", "Hannah", "Ianey", "Michael", "Ivan"],
        "Conner"
    ],

    ["SB Water", 2.60,
        ["Kevin", "Christian", "Payvand", "Nolan", "Bridget", "Christian", "Hannah", "Steph", "Ianey", "Michael", "Ivan", "Chris"],
        "Hannah"
    ],

    ["SB Butter", 3,
        ["Christian", "Ianey", "Michael", "Ivan", "Chris", "Payvand", "Nolan", "Bridget",],
        "Hannah"
    ],

    ["Plastic Bags", 3,
        ["Ianey", "Michael", ],
        "Hannah"
    ],

    ["Oranges", 3,
        ["Ianey", "Michael", ],
        "Hannah"
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
                    + " [$" + str(item[1]) + " / " + str(len(item[2])) + " People] "
                    + " for "
                    + item[0]
                    + " paid to: "
                    + item[3]
                    + "\n"
                    # + "\n       [Calculation: "
                    # + "$" + str(item[1]) + " / " + str(len(item[2])) + " People]\n"
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
                "\n   Price to PAY TO "
                + paidPerson
                + ": $"
                + str("{0:.2f}".format(payAmountTo[paidPerson]))

                )

        result.append(
            "\n\n   Total Price for "
            + person
            + ": $"
            + str("{0:.2f}".format(totalPricePerPerson))

            )
        result.append("\n\n\n\n")
    
    return result


priceList = receiptCalculator(items)

f = open('realOutput.txt', 'w')
for price in priceList:
    f.write(price)
f.close()

