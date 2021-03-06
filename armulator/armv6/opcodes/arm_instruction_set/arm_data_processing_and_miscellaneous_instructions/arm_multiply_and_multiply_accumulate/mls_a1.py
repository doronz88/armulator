from armulator.armv6.opcodes.abstract_opcodes.mls import Mls
from armulator.armv6.opcodes.opcode import Opcode


class MlsA1(Mls, Opcode):
    def __init__(self, instruction, m, a, d, n):
        Opcode.__init__(self, instruction)
        Mls.__init__(self, m, a, d, n)

    def is_pc_changing_opcode(self):
        return False

    @staticmethod
    def from_bitarray(instr, processor):
        rn = instr[-4:]
        rm = instr[20:24]
        ra = instr[16:20]
        rd = instr[12:16]
        if rd.uint == 15 or rm.uint == 15 or rn.uint == 15 or ra.uint == 15:
            print "unpredictable"
        else:
            return MlsA1(instr, **{"m": rm.uint, "a": ra.uint, "d": rd.uint, "n": rn.uint})
