import string
import struct


def u16(buf, off):
    return struct.unpack("<H", buf[off:off+2])[0]


def u32(buf, off):
    return struct.unpack("<I", buf[off:off+4])[0]


def c_str(buf, off):
    end = buf.find(b'\0', off)
    if end == -1:
        end = len(buf)
    return buf[off:end].decode('utf-8', 'ignore')


def hexdump(src, length=16, sep='.'):
    DISPLAY = string.digits + string.ascii_letters + string.punctuation
    FILTER = ''.join([(chr(x) if chr(x) in DISPLAY else '.') for x in range(256)])
    lines = []
    for c in range(0, len(src), length):
        chars = src[c:c+length]
        hex_str = ' '.join([f"{b:02x}" for b in chars])
        if len(hex_str) > 24:
            hex_str = f"{hex_str[:24]} {hex_str[24:]}"
        printable = ''.join([FILTER[b] for b in chars])
        lines.append(f"{c:08x}:  {hex_str:<{length*3}}  |{printable}|\n")
    print(''.join(lines))
