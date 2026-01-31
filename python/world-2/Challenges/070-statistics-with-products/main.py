i = 0
total_money = 0
least_expensive_product = ''
least_expensive_product_price = float('inf')
more_than_1000_count = 0

while True:
    product_name = input("Enter the product name: ")
    
    while True:
        raw_price = input("Enter the product price: $")
        if raw_price.replace('.', '', 1).isdigit():
            product_price = float(raw_price)
            break
        print("Invalid price! Please enter a numeric value.")

    total_money += product_price

    if product_price > 1000:
        more_than_1000_count += 1

    if product_price < least_expensive_product_price:
        least_expensive_product = product_name
        least_expensive_product_price = product_price

    while True:
        continue_choice = input('Do you want to continue? (Y/N): ').strip().upper()
        if continue_choice in ['Y', 'N']:
            break
        print('Please type Y or N.')

    if continue_choice == 'N':
        break

    i += 1

print(f'Total money spent on products: ${total_money:.2f}')
print(f'Number of products costing more than $1000: {more_than_1000_count}')
print(f'The least expensive product is "{least_expensive_product}" costing ${least_expensive_product_price:.2f}')
