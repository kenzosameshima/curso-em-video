import math

str_opposite_side = input("Enter the length of the opposite side: ")
str_adjacent_side = input("Enter the length of the adjacent side: ")
opposite_side = float(str_opposite_side)
adjacent_side = float(str_adjacent_side)

# hypotenuse = (opposite_side**2 + adjacent_side**2) ** 0.5
hypotenuse = math.hypot(opposite_side, adjacent_side)
print(f"The length of the hypotenuse is: {hypotenuse:.2f}")