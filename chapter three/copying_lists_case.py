my_pizza = ["No cheese", "No meat", "just veggies"]
friend_pizzas  = my_pizza[:]
print(f"My pizzas have {my_pizza}")
print(f"My friend's pizzas have {friend_pizzas}")
my_pizza.append('maybe fruits')
friend_pizzas.append('maybe pineapple')
print (my_pizza)
print (friend_pizzas)
for pizza in my_pizza:
    print(f"I like {pizza} on my pizza")
for f_pizza in friend_pizzas:
    print(f"My friend likes {f_pizza} on his pizza")