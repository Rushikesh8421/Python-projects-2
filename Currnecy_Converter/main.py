with open("file.txt") as f:
    lines = f.readlines()

dic_currency = {}
for line in lines:
    parsed = line.split("\t")
    dic_currency[parsed[0]] = parsed[1]

amount = int(input("Enter the amount in rupees that to be converted: "))
print("The options are:\n")
for item in dic_currency.keys():
    print(item)
currency = str(input("Enter the one of the value to be converted into: "))
print(
    f"{amount} INR is equal to {amount*float(dic_currency[currency])} {currency}")
