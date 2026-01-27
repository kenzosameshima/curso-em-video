# attempt to redo the challenge 0180_sin_cos_tan without math lib

str_x = input("Enter an angle in degrees: ")
x = float(str_x)

# Constants
pi = 3.14159265358979323846

# Convert degrees to radians
x_rad = x * (pi / 180)
# Reduce angle to [-pi, pi] for better accuracy
x_rad = ((x_rad + pi) % (2 * pi)) - pi

# Maclaurin series approximations
sin_x = (
    x_rad
    - (x_rad**3) / 6
    + (x_rad**5) / 120
    - (x_rad**7) / 5040
    + (x_rad**9) / 362880
    - (x_rad**11) / 39916800
)

cos_x = (
    1
    - (x_rad**2) / 2
    + (x_rad**4) / 24
    - (x_rad**6) / 720
    + (x_rad**8) / 40320
    - (x_rad**10) / 3628800
)

# Tangent (watch out near cos = 0)
if abs(cos_x) < 1e-6:
    print("tan(x) is undefined (cos(x) ≈ 0)")
else:
    tan_x = sin_x / cos_x
    print("sin(x) ≈", sin_x)
    print("cos(x) ≈", cos_x)
    print("tan(x) ≈", tan_x)