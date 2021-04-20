"""
    Project By: Rushikesh Patil;
    Description: A grocery billing application to display and sum total bill using Python;
"""

def sum_single(quantity, price):
    return price*quantity;
mylist = [];
suma = 0;
new_item = "y"

while new_item == "y":
    
    print("...Guruprasad Grocery...")
    item = input("Enter the name of item: ");
    quantity = int(input(f"Enter the Quantity of {item}: "));
    price = int(input(f"Enter the prince per unit item of {item}: "));
    total = sum_single(price, quantity);
    suma = suma+total;
    mylist.append(f"{item} of quantity {quantity} so {price}*{quantity} = {total}")
    new_item = str(input("Want to add new item y/n: "));

print(".....🛍️WELCOME TO GURUPRASAD GROCERIES🛍️.....")
for i in mylist:
    print(i);
    
print(f"THE TOTAL BILL IS ₹ {suma}/-only.\nThanks for shopping with us 🙏🙏, have a nice day! 😊😊")
        