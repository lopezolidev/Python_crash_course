def sandwich_order(*ingredients):
    """Shows the ingredients asked in a sandwich"""
    print("\nYou ordered a sandwich with the following:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


sandwich_order('tomato', 'swiss cheese', 'olive oil')
print('----------------------------------------------------------------------')

sandwich_order('glazed onions', 'pastrami')
print('----------------------------------------------------------------------')

sandwich_order('pepperoni')
print('----------------------------------------------------------------------')

