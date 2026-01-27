str_num1 = input("Enter the first number: ")
str_num2 = input("Enter the second number: ")

num1 = float(str_num1)
num2 = float(str_num2)

sum_result = round(num1 + num2, 2)

print(f"The sum is {sum_result:g}")
