#zadanie1
shopping_list={
    "piekarnia": ["bagietka", "kajzerka", "grahamka","chałka"],
    "warzywiak": ["marchewka", "cebula","sałata"],
    "mięsny": ["schab", "szynka"]
}
number_of_products=[]
for shop, products in shopping_list.items():
    for n in products:
        Products=[]
        for n in products:
            Products.append(n.capitalize())
    print(f"Idę do {shop.capitalize()} i kupuję tam: {Products}")
    number_of_products.append(len(products))
print("W sumie kupuję " + str(sum(number_of_products))+" produktów")

print("zadanie zakończone!........test")