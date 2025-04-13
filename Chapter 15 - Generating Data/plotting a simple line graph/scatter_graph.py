import matplotlib.pyplot as plt
import sys


def main() -> None:

    plt.style.use('seaborn-v0_8-talk')

    # Values
    x_values = range(1, 11)
    y_values = [n ** 2 for n in x_values]

    fig, ax = plt.subplots()

    # To plot a single point:
    ax.scatter(5.5, 64, s=500, color='red')

    # To plot a series of points (I used a "colormap", a series of colors in a gradient
    # that moves from a starting to an ending color):
    ax.scatter(x_values, y_values, s=200, c=y_values, cmap=plt.cm.Blues)

    # Set the range of each axis (min_x_axis, max_x_axis, min_y_axis, max_y_axis)
    ax.axis([0, 10.5, 0, 105])

    while True:

        choice = input("Enter 'see' to see the file or 'save' to save the file  - ").strip().lower()

        if choice == 'see':
            plt.show()
            sys.exit()

        elif choice == 'save':
            plt.savefig("Paolo_plot.png")
            sys.exit()

        else:
            print("Wrong input!")


if __name__ == '__main__':
    main()
