def convert_ticket(seat_id):
    binary = seat_id.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(binary, 2)


def main():
    f = open("input.txt", "r")
    inp = f.read().split('\n')
    seat_ids = [convert_ticket(seat_id) for seat_id in inp]
    print(max(seat_ids))


if __name__ == '__main__':
    main()
