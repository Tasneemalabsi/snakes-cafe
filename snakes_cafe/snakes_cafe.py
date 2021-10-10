print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
menu = {
    'wings' : 0,
    'cookies' : 0,
    'spring rolls' : 0,
    'salmon' : 0,
    'steak' : 0,
    'meat tornado' : 0,
    'a literal garden' : 0,
    'ice cream' : 0,
    'cake' : 0,
    'pie' : 0,
    'coffee' : 0,
    'tea' : 0,
    'unicorn tears' : 0
}

order = input("what's your order ?  ")

while order != "quit":
    
    if order in menu:
        menu[order] += 1
        for i in menu:
            if menu[order] >= 1:
                print(f'**{menu[order]} order of {order} have been added to your meal **')
    else:
        print("your order is not in the menu, order again please ")
        order= input("what's your order ?  ")

