from typing import Dict, Union, Callable, Tuple

import aoc20.comp.operations.operations as op
import aoc20.comp.ExecutionContext as ec
from collections import defaultdict

from aoc20.comp.ExecutionContext import ExecutionContext


def parse(program):
    ins_arr = program.split('\n')
    memory: Dict[str, Tuple[Callable[[ExecutionContext, str], None], str]] = defaultdict(lambda: ())
    for index, ins in enumerate(ins_arr):
        memory[str(index)] = parse_instruction(ins)
    return memory
    # return [parse_instruction(ins) for ins in ins_arr]


instruction_fn_map: Dict[str, Union[Callable[[ExecutionContext, str], None]]] = {
    'acc': op.accumulator,
    'jmp': op.jump,
    'nop': op.nop,
}


def parse_instruction(instruction: str):
    instruction_end = instruction.index(' ')
    op_code = instruction[0:instruction_end]
    argument = instruction[instruction_end:]
    return instruction_fn_map[op_code], argument


class Program:
    def __init__(self, program: str):
        self._program = parse(program)

    def get_ins_at(self, index: str):
        index = str(index)
        return self._program[index]

    def set_ins_at(self, index: str, value: Tuple[Callable[[ExecutionContext, str], None], str]):
        index = str(index)
        self._program[index] = value

    def start(self):
        visited_loc = set()

        computer = ec.ExecutionContext()

        while True:
            if computer.cur == len(self._program):
                return 0, computer
            if computer.cur in visited_loc:
                return None
            parse_pgm = self.get_ins_at(computer.cur)
            visited_loc.add(computer.cur)
            instruction, argument = parse_pgm
            instruction(computer, argument)



