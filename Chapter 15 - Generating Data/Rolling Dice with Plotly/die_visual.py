from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


def main() -> None:

    die = Die()

    results = [die.roll() for _ in range(1000)]

    frequencies = [results.count(i) for i in range(1, die.sides + 1)]

    x_values = list(range(1, die.sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequenct of Result'}

    my_layout = Layout(title='Result of rolling die',
                       xaxis=x_axis_config,
                       yaxis=y_axis_config)

    offline.plot(
        {
            'data': data,
            'layout': my_layout,
        },
        filename='die.html'
    )


if __name__ == '__main__':
    main()
