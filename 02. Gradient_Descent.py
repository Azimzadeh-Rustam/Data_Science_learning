import random

def main():
    LEARNING_RATE = 0.001
    ITERATIONS = 100_000

    x = random.randint(-15, 15)

    for i in range(ITERATIONS):
        d_x = df_dx(x)
        x -= LEARNING_RATE * d_x

    print(x, f(x))


def f(x):
    return (x - 3) ** 2 + 4

def df_dx(x):
    return 2 * (x - 3)

if __name__ == '__main__':
    main()
