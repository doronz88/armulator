from armulator.armv6.opcodes.abstract_opcodes.smmls import Smmls
from armulator.armv6.opcodes.opcode import Opcode


class SmmlsA1(Smmls, Opcode):
    def __init__(self, instruction, round_, m, a, d, n):
        Opcode.__init__(self, instruction)
        Smmls.__init__(self, round_, m, a, d, n)

    def is_pc_changing_opcode(self):
        return False

    @staticmethod
    def from_bitarray(instr, processor):
        rn = instr[28:32]
        round_ = instr[26]
        rm = instr[20:24]
        ra = instr[16:20]
        rd = instr[12:16]
        if rd.uint == 15 or rn.uint == 15 or rm.uint == 15 or ra.uint == 15:
            print "unpredictable"
        else:
            return SmmlsA1(instr, **{"round_": round_, "m": rm.uint, "a": ra.uint, "d": rd.uint, "n": rn.uint})
