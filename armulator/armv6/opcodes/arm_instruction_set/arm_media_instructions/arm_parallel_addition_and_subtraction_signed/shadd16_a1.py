from armulator.armv6.opcodes.abstract_opcodes.shadd16 import Shadd16
from armulator.armv6.opcodes.opcode import Opcode


class Shadd16A1(Shadd16, Opcode):
    def __init__(self, instruction, m, d, n):
        Opcode.__init__(self, instruction)
        Shadd16.__init__(self, m, d, n)

    def is_pc_changing_opcode(self):
        return False

    @staticmethod
    def from_bitarray(instr, processor):
        rm = instr[28:32]
        rd = instr[16:20]
        rn = instr[12:16]
        if rd.uint == 15 or rn.uint == 15 or rm.uint == 15:
            print("unpredictable")
        else:
            return Shadd16A1(instr, **{"m": rm.uint, "d": rd.uint, "n": rn.uint})
