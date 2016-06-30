import matplotlib.pyplot as plt

data = open("results.csv").readlines()[1:]


def plot(title, x, y, plots):
    my_plot, = plt.plot(x, y)
    plots.append((my_plot, title))


def plot_delay(desired_speed):
    plt.cla()
    plt.clf()
    delays = {}
    for i in xrange(len(data)):
        row = [float(x.strip()) for x in data[i].split(',')]
        speed = row[0]
        if speed != desired_speed:
            continue
        delay = row[1]
        light_length = row[2]
        percent = row[-1]
        if delay not in delays:
            delays[delay] = {}
            delays[delay]['x'] = list()
            delays[delay]['y'] = list()
        delays[delay]['x'].append(light_length)
        delays[delay]['y'].append(percent)

    plots = []
    for x in delays.keys():
        if x not in {0, 3, 5, 7, 10}:
            continue
        title = "%s delay" % x
        plot(title, delays[x]['x'], delays[x]['y'], plots)
    plt.legend(tuple([x[0] for x in plots]), tuple([x[1] for x in plots]), loc='best')
    plt.title("At Speed = %s" % desired_speed)
    plt.xlabel("Seconds of Light")
    plt.ylabel("Percentage of Time Saved")
    plt.savefig("img/light_seconds_speed_%s.png" % desired_speed)


def plot_light(desired_speed):
    plt.cla()
    plt.clf()
    light_lengths = {}
    for i in xrange(len(data)):
        row = [float(x.strip()) for x in data[i].split(',')]
        speed = row[0]
        if speed != desired_speed:
            continue
        delay = row[1]
        light_length = row[2]
        percent = row[-1]
        if light_length not in light_lengths:
            light_lengths[light_length] = {}
            light_lengths[light_length]['x'] = list()
            light_lengths[light_length]['y'] = list()
        light_lengths[light_length]['x'].append(delay)
        light_lengths[light_length]['y'].append(percent)

    plots = []
    for x in light_lengths.keys():
        if x not in {30, 45, 60, 75, 90}:
            continue
        title = "%s second delay" % x
        plot(title, light_lengths[x]['x'], light_lengths[x]['y'], plots)
    plt.legend(tuple([x[0] for x in plots]), tuple([x[1] for x in plots]), loc='best')
    plt.title("At Speed = %s" % desired_speed)
    plt.xlabel("Delay Seconds")
    plt.ylabel("Percentage of Time Saved")
    plt.savefig("img/durations_speed_%s.png" % desired_speed)


def plot_speed(args):
    """
    :param args:  A set of (light_length, delay) tuples
    :return:
    """
    plt.cla()
    plt.clf()
    speeds = {}
    for i in xrange(len(data)):
        row = [float(x.strip()) for x in data[i].split(',')]
        speed = row[0]
        delay = row[1]
        light_length = row[2]
        key = (light_length, delay)
        if key not in args:
            continue
        percent = row[-1]
        if key not in speeds:
            speeds[key] = {'x': [], 'y': []}
        speeds[key]['x'].append(speed)
        speeds[key]['y'].append(percent)


    plots = []
    for x in speeds.keys():
        if x not in args:
            continue
        title = "light_length=%s,delay=%s" % x
        plot(title, speeds[x]['x'], speeds[x]['y'], plots)
    plt.legend(tuple([x[0] for x in plots]), tuple([x[1] for x in plots]), loc='best')
    plt.title("Speeds")
    plt.xlabel("Speed MPH")
    plt.ylabel("Percentage of Time Saved")
    plt.savefig("img/speed_vs_time.png")


def main():
    plot_delay(3.1)
    plot_delay(4.0)
    plot_light(3.1)
    plot_light(4.0)
    plot_speed({(40.0, 5.0), (45, 5.0), (50, 5.0)})


if __name__ == "__main__":
    main()
