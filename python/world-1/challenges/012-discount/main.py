str_price = input('What is the price of the product? $ ')
price = float(str_price)

discounted_price = price * (0.05)
new_price = price - discounted_price

print(f'The product costed $ {price:.2f}, with a 5% discount (${discounted_price:.2f}) it will now cost $ {new_price:.2f}.')
