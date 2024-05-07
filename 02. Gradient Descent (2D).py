import random
import matplotlib.pyplot as plt
import numpy as np


def main():
    LEARNING_RATE = 0.1
    ITERATIONS = 20

    x = random.randint(0, 6)

    x_plt = np.arange(0, 6, 0.1)
    f_plt = [f(x) for x in x_plt]

    plt.ion()
    fig, ax = plt.subplots()
    ax.grid(True)

    ax.plot(x_plt, f_plt)
    point = ax.scatter(x, f(x), c='red')

    for _ in range(ITERATIONS):
        d_x = df_dx(x)
        x -= LEARNING_RATE * d_x

        point.set_offsets([x, f(x)])

        fig.canvas.draw()
        fig.canvas.flush_events()

    plt.ioff()
    print(x, f(x))
    ax.scatter(x, f(x), c='blue')
    plt.show()


def f(x):
    return (x - 3) ** 2 + 4


def df_dx(x):
    return 2 * (x - 3)
    #return lambdify(diff())


if __name__ == '__main__':
    main()
