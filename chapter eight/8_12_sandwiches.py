def make_sw(*fillings):
    """Returns the options the customer took in a neat summary"""
    print(f"\nMaking a sandwich with your selected fillings:")
    for filling in fillings:
        print(f" - {filling.title()}")
    print(f"Thank you for your purchase.")

make_sw("tofu", "tomato", "more vegetables")
make_sw("vegetarian stuff 1",
         "vegetarian stuff 2",
           "vegetarian stuff 3"
           )
make_sw("other stuff 1",
         "other stuff 2",
           "other stuff 3"
           )