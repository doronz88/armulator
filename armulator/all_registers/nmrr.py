from bitstring import BitArray


class NMRR(object):
    """
    Normal Memory Remap Register
    """

    def __init__(self):
        self.value = BitArray(length=32)

    def set_ir_n(self, n, ir):
        assert n < 8
        self.value[30 - (2 * n):32 - (2 * n)] = ir

    def get_ir_n(self, n):
        assert n < 8
        return self.value[30 - (2 * n):32 - (2 * n)]

    def set_or_n(self, n, or_):
        assert n < 8
        self.value[14 - (2 * n):16 - (2 * n)] = or_

    def get_or_n(self, n):
        assert n < 8
        return self.value[14 - (2 * n):16 - (2 * n)]
