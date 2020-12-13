import aoc20.comp.operations.operations as op
import aoc20.comp.Program as pgm

def main():
    f = open("input.txt", "r")
    inp = f.read().strip()

    res = None
    i = 0
    while res is None:
        program = pgm.Program(inp)
        (op_code, argument) = program.get_ins_at(i)

        if (op_code != op.nop) & (op_code != op.jump):
            i += 1
            continue
        if op_code == op.nop:
            program.set_ins_at(i, (op.jump, argument))
        else:
            program.set_ins_at(i, (op.nop, argument))
        res = program.start()
        i += 1

    print(i)
    (res, cmp) = res
    print(cmp.accumulator)


if __name__ == '__main__':
    main()
