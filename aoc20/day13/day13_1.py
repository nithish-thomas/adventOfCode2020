

def main():
    f = open("input.txt", "r")
    leave_time = int(f.readline())
    bus_id_arr = f.readline().split(',')
    bus_id_arr = list(filter(lambda x: x != 'x', bus_id_arr))
    bus_id_arr = [int(number) for number in bus_id_arr]
    bus_id_arr = sorted(bus_id_arr)

    depart_time = leave_time
    while True:
        for bus_id in bus_id_arr:
            if depart_time % bus_id == 0:
                print(bus_id)
                print(depart_time)
                print(bus_id * (depart_time- leave_time))
                return
        depart_time += 1








if __name__ == "__main__":
    main()
