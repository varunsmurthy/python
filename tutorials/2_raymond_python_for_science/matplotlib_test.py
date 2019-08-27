from numpy import *
from matplotlib import pyplot


def create_test_plot():
    x = arange(0, 4 * pi, 0.1)

    a = sin(x)
    b = cos(x)
    c = tan(x)
    d = x

    pyplot.figure(figsize=(10, 8))
    pyplot.subplots_adjust(hspace=0.4, wspace=0.4)

    pyplot.subplot(2, 2, 1)
    pyplot.plot(x, a, "r-", linewidth=1, label="sine")
    pyplot.title("sine function")
    pyplot.xlabel("radians")
    pyplot.ylabel("y")
    pyplot.axis([0, 4.1 * pi, -2, 2])
    pyplot.grid(True)
    pyplot.legend()

    pyplot.subplot(2, 2, 2)
    pyplot.plot(x, b, "k-", linewidth=2, label="cosine")
    pyplot.title("cosine function")
    pyplot.xlabel("radians")
    pyplot.ylabel("y")
    pyplot.axis([0, 4.1 * pi, -2, 2])
    pyplot.grid(True)
    pyplot.legend()

    pyplot.subplot(2, 2, 3)
    pyplot.plot(x, c, "b-", linewidth=3, label="tangent")
    pyplot.title("tangent function")
    pyplot.xlabel("radians")
    pyplot.ylabel("y")
    pyplot.axis([0, 4.1 * pi, -2, 2])
    pyplot.grid(True)
    pyplot.legend()

    pyplot.subplot(2, 2, 4)
    pyplot.plot(x, d, "g-", linewidth=1, label="linear")
    pyplot.title("linear function")
    pyplot.xlabel("radians")
    pyplot.ylabel("y")
    pyplot.axis([0, 4.1 * pi, 0, 4.1 * pi])
    pyplot.grid(True)
    pyplot.legend()

    pyplot.show()


def main():
    create_test_plot()


if __name__ == "__main__":
    main()