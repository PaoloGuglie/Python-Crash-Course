import matplotlib.pyplot as plt


def main() -> None:

    numbers = [n for n in range(1, 6)]

    squares = [n ** 2 for n in range(1, 6)]

    # The subplots() function can generate one or more plots in the same figure.
    # The variable "fig" represents the entire figure or collection of plots that
    # are generated.
    # The variable "ax" represents a single plot in the figure and is the variable
    # I will use.
    fig, ax = plt.subplots()

    # Plot the data (if I only give the "squares" sequence, plot() assumes the first data point
    # corresponds to an x-coordinate value of 0, but my first data point corresponds
    # to an x-value of 1; I can also give the "numbers" sequence to override the default
    # behavior).
    ax.plot(numbers, squares, linewidth=3)

    # Set chart title and label axes
    ax.set_title("SQUARES", fontsize=20)
    ax.set_xlabel("VALUE", fontsize=14)
    ax.set_ylabel("SQUARE", fontsize=14)

    # Set size of tick labels
    ax.tick_params(axis='both', labelsize=12)

    plt.show()


if __name__ == '__main__':
    main()
