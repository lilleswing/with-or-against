################## Constants ################################
RED = "RED"
GREEN = "GREEN"
DISTANCE = 2  # miles, arbitrary

MIN_SPEED = 3.0
MAX_SPEED = 4.0
SPEED_STEP = 0.1

BLOCKS_PER_MILE = 20

DELAY_MIN = 0
DELAY_MAX = 10
DELAY_STEP = 1

# Assume Symmetric Lights -- This is wrong and implementation already exists for specific red/green lengths
LIGHT_LENGTH_MIN = 30
LIGHT_LENGTH_MAX = 90
LIGHT_LENGTH_STEP = 15


#############################################################


class TrafficLight:
    def __init__(self, location, delay, red_length, green_length, speed):
        self.location = location
        self.delay = delay
        self.red_length = red_length
        self.green_length = green_length
        self.period = self.red_length + self.green_length
        self.speed = speed

    def get_status(self, since_epoch):
        period_time = (since_epoch - self.delay + self.period) % self.period
        if period_time < self.green_length:
            return GREEN
        return RED


def get_intersection(old_location, new_location, intersections):
    for loc in intersections:
        if old_location < loc.location < new_location:
            return loc
    return None


class Simulation:
    def __init__(self, delay, red_length, green_length):
        self.delay = delay
        self.red_length = red_length
        self.green_length = green_length

    def simulate(self, with_traffic=True):
        stuck_at_light_count = 0
        delay = self.delay
        if not with_traffic:
            delay *= -1
        intersections = []
        intersection_loc = 1.0 / BLOCKS_PER_MILE
        while intersection_loc < DISTANCE:
            intersections.append(
                TrafficLight(intersection_loc, delay * len(intersections), self.red_length, self.green_length))
            intersection_loc += 1.0 / BLOCKS_PER_MILE

        total_seconds = 0
        total_stuck_at_light_count = 0
        for i in xrange(0, intersections[0].period):
            old_loc = 0
            seconds = i
            while old_loc < DISTANCE:
                new_loc = old_loc + self.speed
                crossed_intersection = get_intersection(old_loc, new_loc, intersections)
                if crossed_intersection is None or crossed_intersection.get_status(seconds) == GREEN:
                    old_loc = new_loc
                else:
                    stuck_at_light_count += 1
                seconds += 1
            total_seconds += seconds - i
            total_stuck_at_light_count += stuck_at_light_count
        return (float(total_seconds) / float(intersections[0].period),
                float(total_stuck_at_light_count) / float(intersections[0].period))


def main():
    print("speed, delay, light_length, seconds_with, seconds_against, time_saved, time_saved_percent")
    for delay in xrange(DELAY_MIN, DELAY_MAX + 1, DELAY_STEP):
        for light_length in xrange(LIGHT_LENGTH_MIN, LIGHT_LENGTH_MAX + 1, LIGHT_LENGTH_STEP):
            speed = MIN_SPEED
            while speed <= MAX_SPEED:
                sim = Simulation(delay, light_length, light_length, speed)
                seconds_with, stuck_at_light_with = sim.simulate(True)
                seconds_against, stuck_at_light_against = sim.simulate(False)
                difference = seconds_against - seconds_with
                percent = difference / float(seconds_against)
                print("%s, %s,%s,%s,%s,%s,%s" %
                      (speed, delay, light_length, seconds_with, seconds_against, difference, percent))
                speed += SPEED_STEP


if __name__ == "__main__":
    main()
