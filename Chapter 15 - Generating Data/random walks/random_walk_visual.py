import matplotlib.pyplot as plt
from random_walk import RandomWalk


def create_and_plot_random_walk() -> None:
    """ Generate data from a random walk and plot it using scatters """

    rw = RandomWalk()
    rw.walk()

    fig, ax = plt.subplots()

    # scatter the points using a colormap to show the path
    ax.scatter(rw.x_values,
               rw.y_values,
               s=3,
               c=rw.x_values,
               cmap=plt.cm.Blues,
               edgecolors='none')

    # emphasize the first and last points
    ax.scatter(0, 0, color='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], color='red', s=100)

    plt.show()


def main() -> None:

    create_and_plot_random_walk()

    while input("Make another random walk? (q to quit)  - ") != 'q':
        create_and_plot_random_walk()


if __name__ == '__main__':
    main()
