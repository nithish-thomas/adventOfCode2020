from aoc20.day8 import Computer


def accumulator(computer: Computer, argument):
    argument = int(argument)
    computer.accumulator += argument
    computer.cur += 1
