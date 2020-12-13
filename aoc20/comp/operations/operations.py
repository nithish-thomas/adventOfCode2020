from aoc20.comp.ExecutionContext import ExecutionContext


def jump(computer: ExecutionContext, argument: str):
    computer.cur += int(argument)


def accumulator(computer: ExecutionContext, argument: str):
    argument = int(argument)
    computer.accumulator += argument
    computer.cur += 1


def nop(computer: ExecutionContext, _: str):
    computer.cur += 1
