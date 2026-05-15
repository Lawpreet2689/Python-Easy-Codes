menu = {
    'Butter Chicken': 60,
    'Chicken Biryani': 100,
    'Tandoori Naan': 15,
    'Paneer Kadhai': 50,
    'Lassi': 20
}
print("Welcome to the Hotel")
print("Butter Chicken: Rs60\nChicken Biryani: Rs100\nTandoori Naan: Rs15\nPaneer Kadhai: Rs50\nLassi: Rs20")

order_total = 0

item_1 = input("Enter the 1st Item:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added")
else:
    print(f"Ordered item {item_1} is not available")
another_order = input("Do you want something else? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the 2nd Item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added")
    else:
        print(f"Ordered item {item_2} is not available")

print(f"The Total amount of items to pay is {order_total}")        
