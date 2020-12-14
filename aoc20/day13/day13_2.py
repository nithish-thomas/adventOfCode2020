

def main():
    f = open("input.txt", "r")
    f.readline()
    bus_id_arr = f.readline().split(',')
    bus_id_inp = [{k: v} for (k, v) in enumerate(bus_id_arr)]
    bus_id_2_time = {v: k for (k, v) in enumerate(bus_id_arr)}
    bus_id_2_time = {k: v for k, v in bus_id_2_time.items() if k != 'x'}
    bus_id_arr = list(filter(lambda x: x != 'x', bus_id_arr))
    bus_id_arr = [int(number) for number in bus_id_arr]

    max_id = max(bus_id_arr)
    bus_id_arr = list(reversed(sorted(bus_id_arr)))[1:]
    i = 1
    while True:
        time_of_max = max_id * i
        bus_max_rel_time = bus_id_2_time[str(max_id)]
        if other_buses_arrive_on_time(bus_id_2_time, bus_id_arr, bus_max_rel_time, time_of_max):
            print(time_of_max)
            res = []
            for bus_id in bus_id_arr:
                bus_rel_time = bus_id_2_time[str(bus_id)]
                expected_time = time_of_max + bus_rel_time - bus_max_rel_time
                res.append(expected_time)
            print(min(res))
            return

        i += 1


def other_buses_arrive_on_time(bus_id_2_time, bus_id_arr, bus_max_rel_time, time_of_max):
    for bus_id in bus_id_arr:
        bus_rel_time = bus_id_2_time[str(bus_id)]
        expected_time = time_of_max + bus_rel_time - bus_max_rel_time
        if expected_time % bus_id != 0:
            return False
    return True


if __name__ == "__main__":
    main()
