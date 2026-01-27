from math import radians, sin, cos, tan

angle = float(input("Enter an angle in degrees: "))
angle_rad = radians(angle)

print(f"Angle in radians: {angle_rad:.10f}\n")
print(f"Sine: {sin(angle_rad):.10f}")
print(f"Cosine: {cos(angle_rad):.10f}")
print(f"Tangent: {tan(angle_rad):.10f}\n")

print(f"cosecant: {1/sin(angle_rad):.10f}")
print(f"secant: {1/cos(angle_rad):.10f}")
print(f"cotangent: {1/tan(angle_rad):.10f}")
