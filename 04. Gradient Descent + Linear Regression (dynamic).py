import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, diff, lambdify
import pandas as pd
import numpy as np


def main():
    LEARNING_RATE = 0.001
    ITERATIONS = 1_000
    TIME_DELAY = 0.1

    k, b = symbols('k b')
    k_value, b_value = 0.0, 0.0

    points = pd.read_csv("https://bit.ly/2KF29Bd")
    X_points = points['x'].values
    Y_points = points['y'].values

    sum_of_squares = sum((k * X_points[i] + b - Y_points[i]) ** 2 for i in range(len(X_points)))
    loss_func = lambdify([k, b], sum_of_squares)

    d_k = diff(sum_of_squares, k)
    d_b = diff(sum_of_squares, b)
    grad_k = lambdify([k, b], d_k)
    grad_b = lambdify([k, b], d_b)

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Add 3D subplot
    ax.set_xlabel('k (slope)')
    ax.set_ylabel('b (intercept)')
    ax.set_zlabel('Loss function')

    # Visualize the error surface
    k_mesh, b_mesh = np.meshgrid(np.linspace(-10, 10, 30), np.linspace(-10, 10, 30))
    loss_mesh = loss_func(k_mesh, b_mesh)
    ax.plot_surface(k_mesh, b_mesh, loss_mesh, cmap='viridis', alpha=0.6)

    # Initial point
    point, = ax.plot([k_value], [b_value], [loss_func(k_value, b_value)], 'ro')

    for _ in range(ITERATIONS):
        k_value -= LEARNING_RATE * grad_k(k_value, b_value)
        b_value -= LEARNING_RATE * grad_b(k_value, b_value)

        # Update the point position
        point.set_data([k_value], [b_value])
        point.set_3d_properties([loss_func(k_value, b_value)])
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(TIME_DELAY)

    plt.ioff()
    print(f"y = {k_value:.3f} * x + {b_value:.3f}")
    point.set_color('b')
    plt.show()


if __name__ == '__main__':
    main()
