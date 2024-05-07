from sympy import *
import pandas as pd


def main():
    LEARNING_RATE = 0.001
    ITERATIONS = 100_000

    k, b = symbols('k b')
    k_value, b_value = 0.0, 0.0

    points = pd.read_csv("https://bit.ly/2KF29Bd")
    X_points = points['x'].values
    Y_points = points['y'].values

    sum_of_squares = sum((k * X_points[i] + b - Y_points[i])**2 for i in range(len(X_points)))

    d_k = diff(sum_of_squares, k)
    d_b = diff(sum_of_squares, b)

    # lambdify - converting from SymPy to an optimized Python function
    grad_k = lambdify([k, b], d_k)
    grad_b = lambdify([k, b], d_b)

    for _ in range(ITERATIONS):
        k_value -= LEARNING_RATE * grad_k(k_value, b_value)
        b_value -= LEARNING_RATE * grad_b(k_value, b_value)

    print(f"y = {k_value:.3f} * x + {b_value:.3f}")


if __name__ == '__main__':
    main()
