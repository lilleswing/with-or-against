import matplotlib.pyplot as plt

data = open("results.csv").readlines()[1:]


def plot(title, x, y, plots):
    my_plot, = plt.plot(x, y)
    plots.append((my_plot, title))


def main():
    delays = {}
    light_lengths = {}
    for i in xrange(len(data)):
        row = [float(x.strip()) for x in data[i].split(',')]
        delay = row[0]
        light_length = row[1]
        percent = row[-1]
        if delay not in delays:
            delays[delay] = {}
            delays[delay]['x'] = list()
            delays[delay]['y'] = list()
        delays[delay]['x'].append(light_length)
        delays[delay]['y'].append(percent)

        if light_length not in light_lengths:
            light_lengths[light_length] = {}
            light_lengths[light_length]['x'] = list()
            light_lengths[light_length]['y'] = list()

        light_lengths[light_length]['x'].append(delay)
        light_lengths[light_length]['y'].append(percent)

    plots = []
    for x in delays.keys():
        if x not in {0, 3, 5, 7, 10}:
            continue
        title = "%s delay" % x
        plot(title, delays[x]['x'], delays[x]['y'], plots)
    plt.legend(tuple([x[0] for x in plots]), tuple([x[1] for x in plots]), loc='best')
    plt.xlabel("Seconds of Light")
    plt.ylabel("Percentage of Time Saved")
    plt.savefig("light_seconds.png")

    plt.cla()
    plt.clf()

    plots = []
    for x in light_lengths.keys():
        if x not in {30, 45, 60, 75, 90}:
            continue
        title = "%s second light" % x
        plot(title, light_lengths[x]['x'], light_lengths[x]['y'], plots)
    plt.legend(tuple([x[0] for x in plots]), tuple([x[1] for x in plots]), loc='best')
    plt.xlabel("Delay Seconds")
    plt.ylabel("Percentage of Time Saved")
    plt.savefig("durations.png")


if __name__ == "__main__":
    main()
