import matplotlib.pyplot as plt
import numpy as np

# Use a dark background style
plt.style.use('dark_background')

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.exp(-x * 0.1)

# Create a figure
plt.figure(figsize=(12, 7))

# Plotting with vivid colors
plt.plot(x, y1, label='sin(x)', color='magenta', linewidth=2, linestyle='--')
plt.plot(x, y2, label='cos(x)', color='cyan', linewidth=2, linestyle='-')
plt.plot(x, y3, label='damped sin(x)', color='orange', linewidth=2, linestyle='-.')

# Shaded area between sin and cos
plt.fill_between(x, y1, y2, color='white', alpha=0.1, label='Area between sin and cos')

# Annotation with arrow
plt.annotate('Peak of sin(x)', xy=(1.57, 1), xytext=(2.5, 1.5),
             arrowprops=dict(facecolor='white', arrowstyle='->'),
             color='white')

# Titles and labels
plt.title('🌌 Colorful Trig Functions on Dark Theme', fontsize=16, color='white')
plt.xlabel('X Axis', fontsize=12, color='white')
plt.ylabel('Y Axis', fontsize=12, color='white')

# Tweak ticks color
plt.tick_params(colors='white')

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()

# Show plot
plt.show()

