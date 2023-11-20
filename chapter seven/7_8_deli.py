sandwich_orders = ["type A", "type B", "type C"]
finished_sandwiches = []

#moving items from list 'sandwich_orders' to list 'finished_sandwiches
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"\nI made you a {current_order} sandwich")
    finished_sandwiches.append(current_order)

#Display all finished_sandwiches
print("\n We finished the following sandwiches:")
for finished_sandwich in sorted(finished_sandwiches):
    print(finished_sandwich)