from typing import List, Tuple
from binascii import hexlify, unhexlify

print("PrettyBinary by @wtdcode is loaded.")

class pb:

    @staticmethod
    def int2bits(v: int, bits_per_line=16, reverse=False):
        def _pb_bits(bits: List[Tuple[int, int]], base=0):
            l = len(bits)
            s = ""
            for i in range(l):
                s += f"{bits[i][0]:4}"
            s += "\n"
            for i in range(l):
                s += "----"
            s += "\n"
            for i in range(l):
                s += f"{bits[i][1]:4}"
            s += "\n"
            print(s)

        width = 0
        while v > (2 ** width):
            width += 8

        bits = []
        idx = 0
        while v != 0:
            bits.append((idx, v & 1))
            v = v >> 1
            idx += 1

        while idx < width:
            bits.append((idx, 0))
            idx += 1

        if not reverse:
            bits.reverse()

        ngroups = (len(bits) - 1 + bits_per_line) // bits_per_line

        print("====" * bits_per_line + "\n")
        for g in range(ngroups):
            _pb_bits(bits[g*bits_per_line:(g+1)*bits_per_line], g*bits_per_line)
            print("====" * bits_per_line + "\n")

    @staticmethod
    def bytes2bits(bs: bytes, big_endian=False):
        be = "big" if big_endian else "little"
        v = int.from_bytes(bs, be)
        pb.int2bits(v)

    @staticmethod
    def hex(bs: bytes):
        return hexlify(bs)
    
    @staticmethod
    def unhex(s: str):
        return unhexlify(s)
    
    @staticmethod
    def bytes2c(bs: bytes):
        bs = list(bs)

        print("".join(map(lambda x: f"\\x{x:02}", bs)))
