product_price = float(input('Product price: $').strip().replace(',', '.'))

print('Payment methods:')
print('[ 1 ] Cash/Check')
print('[ 2 ] Credit Card (immediate payment)')
print('[ 3 ] Credit Card (installments)')

payment_option = int(input('Choose a payment option (1-3): '))

if payment_option == 1:
    final_price = product_price * 0.90
    print(f'Final price with 10% discount: ${final_price:.2f}')

elif payment_option == 2:
    final_price = product_price * 0.95
    print(f'Final price with 5% discount: ${final_price:.2f}')

elif payment_option == 3:
    installments = int(input('Number of installments (1-12): '))

    if 1 <= installments <= 2:
        final_price = product_price
        print(f'Final price: ${final_price:.2f}')

    elif installments <= 6:
        interest = 1.20
        final_price = product_price * interest
        installment_amount = final_price / installments
        print(f'Final price with 20% interest: ${final_price:.2f}')
        print(f'Installment amount: ${installment_amount:.2f} over {installments} months')

    elif installments <= 12:
        interest = 1.35
        final_price = product_price * interest
        installment_amount = final_price / installments
        print(f'Final price with 35% interest: ${final_price:.2f}')
        print(f'Installment amount: ${installment_amount:.2f} over {installments} months')

    else:
        print('Invalid number of installments. Please choose between 1 and 12.')

else:
    print('Invalid payment option. Please choose between 1 and 3.')
