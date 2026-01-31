for i in range(5):
    str_weight = input(f'Enter the weight of person {i+1} (in kg): ')
    weight = float(str_weight)
    if i == 0:
        heaviest = weight
        lightest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lightest:
            lightest = weight

print(f'The heaviest weight is {heaviest} kg.')
print(f'The lightest weight is {lightest} kg.')
