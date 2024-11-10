import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# Define the degrees and convert to radians
degrees = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
radians = [np.deg2rad(deg) for deg in degrees]

# Set up unit circle
circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.add_artist(circle)

# Plot points on the unit circle and annotate them
for deg, rad in zip(degrees, radians):
    x, y = np.cos(rad), np.sin(rad)
    ax.plot(x, y, 'o', color='blue')
    # Display the degree and radian values as fractions
    ax.text(x * 1.1, y * 1.1, f"{deg}°\n{Fraction(rad).limit_denominator()}π", ha='center', color='black')

# Set axis limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', 'box')
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# Label for axes
ax.set_xlabel('cos(θ)')
ax.set_ylabel('sin(θ)')
ax.set_title('Unit Circle with Selected Degrees and Radians')

# Show the plot
plt.show()
