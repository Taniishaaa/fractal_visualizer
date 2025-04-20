import numpy as np

def mandelbrot(width, height, zoom, x_center, y_center, max_iter):
    x = np.linspace(x_center - 1.5/zoom, x_center + 1.5/zoom, width)
    y = np.linspace(y_center - 1.0/zoom, y_center + 1.0/zoom, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    img = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        img[mask] = i
    return img

def julia(width, height, zoom, x_center, y_center, max_iter, c=-0.8 + 0.156j):
    x = np.linspace(x_center - 1.5/zoom, x_center + 1.5/zoom, width)
    y = np.linspace(y_center - 1.0/zoom, y_center + 1.0/zoom, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] ** 2 + c
        img[mask] = i
    return img
