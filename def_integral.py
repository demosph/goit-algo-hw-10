import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
     return x**2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла за допомогою методу Монте-Карло
num_samples = 1000000
x_samples = np.random.uniform(a, b, num_samples)
integral_mc = (b - a) * np.mean(f(x_samples))

# Обчислення інтеграла за допомогою функції quad
intergral_quad, error = spi.quad(f, a, b)

# Виведення результатів
print("Інтеграл (Монте-Карло): {:.6f}".format(integral_mc))
print("Інтеграл (quad): {:.6f}".format(intergral_quad))

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()