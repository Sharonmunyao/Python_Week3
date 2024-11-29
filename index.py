def calculate_discount():
    price = int(input("Hi User, please enter the Original price:"))
    discount_percent = float(input("Also, kindly enter the discount quoted:"))

    final_price = price - (price * discount_percent)

    if discount_percent >= 0.2:
        print (f'After the discount, please pay {final_price}')
    else: 
        print (f'The price remains to be {price}')

calculate_discount()

    