from armulator.armv6.opcodes.abstract_opcodes.udiv import Udiv
from armulator.armv6.opcodes.opcode import Opcode


class UdivA1(Udiv, Opcode):
    def __init__(self, instruction, m, d, n):
        Opcode.__init__(self, instruction)
        Udiv.__init__(self, m, d, n)

    def is_pc_changing_opcode(self):
        return False

    @staticmethod
    def from_bitarray(instr, processor):
        rn = instr[28:32]
        rm = instr[20:24]
        rd = instr[12:16]
        if rd.uint == 15 or rn.uint == 15 or rm.uint == 15:
            print "unpredictable"
        else:
            return UdivA1(instr, **{"m": rm.uint, "d": rd.uint, "n": rn.uint})
