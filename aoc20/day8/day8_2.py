import Program
from aoc20.day8.operations import nop
from aoc20.day8.operations import Jump

def main():
    f = open("input.txt", "r")
    inp = f.read().strip()

    res = None
    i = 0
    program = None
    while res is None:
        program = Program.Program(inp)
        (op_code, argument) = program.program[i]

        if (op_code != nop.nop) & (op_code != Jump.jump):
            i += 1
            continue
        if op_code == nop.nop:
            program.program[i] = Jump.jump, argument
        else:
            program.program[i] = nop.nop, argument
        res = program.start()
        i += 1

    print(i)
    (res, cmp) = res
    print(cmp.accumulator)


if __name__ == '__main__':
    main()
