product = input("Please, insert the product name: ")
code = int(input("Type the code: "))
price = float(input("Type the price: "))
amount = int(input("How many: "))
total = amount*price

print(f"You registered {amount} {product} code {code}")
print(f"Total value {total}")