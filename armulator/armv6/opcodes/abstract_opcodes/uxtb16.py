from armulator.armv6.opcodes.abstract_opcode import AbstractOpcode
from armulator.armv6.shift import ror
from armulator.armv6.bits_ops import zero_extend


class Uxtb16(AbstractOpcode):
    def __init__(self, m, d, rotation):
        super(Uxtb16, self).__init__()
        self.m = m
        self.d = d
        self.rotation = rotation

    def execute(self, processor):
        if processor.condition_passed():
            rotated = ror(processor.registers.get(self.m), self.rotation)
            temp_rd = zero_extend(rotated[8:16], 16)
            temp_rd += zero_extend(rotated[24:32], 16)
            processor.registers.set(self.d, temp_rd)
