from armulator.armv6.opcodes.abstract_opcodes.qdsub import Qdsub
from armulator.armv6.opcodes.opcode import Opcode


class QdsubA1(Qdsub, Opcode):
    def __init__(self, instruction, m, d, n):
        Opcode.__init__(self, instruction)
        Qdsub.__init__(self, m, d, n)

    def is_pc_changing_opcode(self):
        return False

    @staticmethod
    def from_bitarray(instr, processor):
        rm = instr[-4:]
        rd = instr[16:20]
        rn = instr[12:16]
        if rd.uint == 15 or rm.uint == 15 or rn.uint == 15:
            print "unpredictable"
        else:
            return QdsubA1(instr, **{"m": rm.uint, "d": rd.uint, "n": rn.uint})
