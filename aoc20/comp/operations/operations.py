from aoc20.comp.Computer import Computer


def jump(computer: Computer, argument: str):
    computer.cur += int(argument)


def accumulator(computer: Computer, argument: str):
    argument = int(argument)
    computer.accumulator += argument
    computer.cur += 1


def nop(computer: Computer, _: str):
    computer.cur += 1