import Program
def main():
    f = open("input.txt", "r")
    inp = f.read().strip()
    program = Program.Program(inp)
    res = program.start()


if __name__ == '__main__':
    main()
