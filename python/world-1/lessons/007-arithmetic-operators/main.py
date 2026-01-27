str_n1 = input('Type a number: ')
str_n2 = input('Type another number: ')

n1 = float(str_n1)
n2 = float(str_n2)

add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
exp = n1 ** n2
int_div = n1 // n2
mod = n1 % n2

print(f'+: {add:.2f}, -: {sub:.2f}, *: {mul:.2f}, /: {div:.2f}, **: {exp:.2f}, //: {int_div:.2f}, %: {mod:.2f}')