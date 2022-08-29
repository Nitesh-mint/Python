def orderPizza(size,style =" regular",topping =None ):
    #check if the topping was specified
    Price_of_topping = 150 #price for any topping

    if size == "small":
        price = 800
    elif size == "medium":
        price = 1000
    else: #large
        price = 1500

    if style == "deepdish ":
        price = price + 200
    
    line = "You have ordered a " +size+style + ' pizza with'

    if topping == None:
        print(line + " no topping")
    
    else:
        print(line + " Topping.")
        price = price + Price_of_topping
    
    print("The price is RS",price)
    print()

orderPizza("large")
orderPizza("small")
orderPizza("small",topping=True, style = "deepdish")
orderPizza("small",topping=True, style = "MOMO")