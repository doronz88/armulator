from armulator.armv6.opcodes.abstract_opcode import AbstractOpcode
from armulator.armv6.bits_ops import zero_extend


class Ubfx(AbstractOpcode):
    def __init__(self, lsbit, widthminus1, d, n):
        super(Ubfx, self).__init__()
        self.lsbit = lsbit
        self.widthminus1 = widthminus1
        self.d = d
        self.n = n

    def execute(self, processor):
        if processor.condition_passed():
            msbit = self.lsbit + self.widthminus1
            if msbit <= 31:
                processor.registers.set(self.d, zero_extend(
                        processor.registers.get(self.n)[31 - msbit:32 - self.lsbit], 32))
            else:
                print "unpredictable"
