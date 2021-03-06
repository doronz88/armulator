from armulator.armv6.opcodes.abstract_opcode import AbstractOpcode
from bitstring import BitArray


class Shadd8(AbstractOpcode):
    def __init__(self, m, d, n):
        super(Shadd8, self).__init__()
        self.m = m
        self.d = d
        self.n = n

    def execute(self, processor):
        if processor.condition_passed():
            sum1 = processor.registers.get(self.n)[24:32].int + processor.registers.get(self.m)[24:32].int
            sum2 = processor.registers.get(self.n)[16:24].int + processor.registers.get(self.m)[16:24].int
            sum3 = processor.registers.get(self.n)[8:16].int + processor.registers.get(self.m)[8:16].int
            sum4 = processor.registers.get(self.n)[0:8].int + processor.registers.get(self.m)[0:8].int
            processor.registers.set(self.d, BitArray(int=sum4, length=9)[0:8] + BitArray(int=sum3, length=9)[
                                                                                     0:8] + BitArray(int=sum2,
                                                                                                     length=9)[
                                                                                            0:8] + BitArray(int=sum1,
                                                                                                            length=9)[
                                                                                                   0:8])
