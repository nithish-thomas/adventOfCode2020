from aoc20.day8 import Computer


def jump(computer: Computer, argument: str):
    computer.cur += int(argument)
