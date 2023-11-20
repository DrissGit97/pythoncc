sandwich_orders = ["type A", "pastrami", "type B", "pastrami", "type C", "pastrami"]
finished_sandwiches = []

#printing that there is no pastrami left
print("There are no Pastrami sandwiches left.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")


print("Our currently available options are:")
for sandwich in sandwich_orders:
    print(f"\n-{sandwich}")