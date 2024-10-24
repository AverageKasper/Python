import numpy as np

a = 2.493
b = 0.911
c = 137.7
d = 62.3

print(f"Tehtävä 1 a) {np.degrees(a)}")
print(f"Tehtävä 1 b) {np.degrees(b)}\n")
print(f"Tehtävä 2 a) {np.radians(c)}")
print(f"Tehtävä 2 b) {np.radians(d)}\n")

list = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

print("Tehtävä 3 lista")
print("_" * 33)
for n in list:
    print(f"| Degree: {n:3} | Radians: {np.radians(n):4.4f} |")
print("¯" * 33) 

print("Tehtävä 2")
# En kirjoita suomeksi, my bad
print(f"Triangles sides are 1.6m and 2.3m. Triangles hypotenuse size: {np.hypot(1.6, 2.3):.2f}m")

