import numpy as np
import matplotlib.pyplot as plt


def estimate_coeff(x, y):
    # number of observations
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # cross-deviation of x
    ss_xy = np.sum(y*x) - n * m_y * m_x

    # deviation of x
    ss_xx = np.sum(x * x) - n * m_x * m_x

    b_1 = ss_xy / ss_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1


def plotter(x, y, b):

    # Plotting actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # Predict response vector
    y_pred = b[0] + b[1]*x

    # plot line of best fit
    plt.plot(x, y_pred, color="g")

    # Labelling axes
    plt.xlabel("X")
    plt.ylabel("Y")

    # Function to show plot
    plt.show()


def main():

    # observation values

    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    b = estimate_coeff(x, y)
    print("Estimated Coefficient:\nb_0= {}\nb_1= {}".format(b[0], b[1]))
    # plotting the graph

    plotter(x, y, b)


if __name__ == '__main__':
    main()

