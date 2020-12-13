from aoc20.day8.operations import nop
from aoc20.day8.operations import Jump
from aoc20.day8.operations import Accumulator
import Computer


def parse(program):
    ins_arr = program.split('\n')
    return [parse_instruction(ins) for ins in ins_arr]


instruction_fn_map = {
    'acc': Accumulator.accumulator,
    'jmp': Jump.jump,
    'nop': nop.nop
}


def parse_instruction(instruction: str):
    instruction_end = instruction.index(' ')
    op_code = instruction[0:instruction_end]
    argument = instruction[instruction_end:]
    return instruction_fn_map[op_code], argument


class Program:
    def __init__(self, program: str):
        self.program = parse(program)

    def start(self):
        visited_loc = set()

        computer = Computer.Computer()

        while True:
            if computer.cur == len(self.program):
                return 0, computer
            if computer.cur in visited_loc:
                return None
            parse_pgm = self.program[computer.cur]
            visited_loc.add(computer.cur)
            instruction, argument = parse_pgm
            instruction(computer, argument)



