str_real = input('How much money do you have in your wallet? R$ ')
real = float(str_real.replace(',', '.'))
dollar = real / 3.27
rest = real % 3.27
print(f'With R$ {real:.2f} you can buy U$ {dollar:.2f} and will have R$ {rest:.2f} left in your wallet.')
