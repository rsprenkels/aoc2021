packet = list(bin(int('1' + open('16.txt').readline(), 16))[3:])
# EE00D40C823060

version_sum = 0

def get_bits(packet, num_bits):
    print(f'get {num_bits} from {len(packet):3}:{"".join(packet)}')
    res = int(''.join(packet[:num_bits]), 2)
    for _ in range(num_bits): packet.pop(0)
    return res

def parse_packet(packet: str) -> int:
    global version_sum
    bits_parsed = 0
    # print(f'packet: {packet}')
    version = get_bits(packet, 3)
    version_sum += version
    type = get_bits(packet, 3)
    print(f'version:{version} type:{type} ', end='')
    if type == 4:
        digits = []
        keep_reading = True
        while keep_reading:
            keep_reading = get_bits(packet, 1) == 1
            digits.append(get_bits(packet, 4))
        print(f'literal_digits: {digits}')
    else:
        length_type = get_bits(packet, 1)
        print(f'length_type:{length_type} ', end='')
        if length_type == 0: # total length in bits
            subpacket_len = get_bits(packet, 15)
            print(f'subpacket_len:{subpacket_len}')
            pl_start = len(packet)
            while len(packet) > pl_start - subpacket_len:
                parse_packet(packet)
        else: # number of subpackets
            num_subpackets = get_bits(packet, 11)
            print(f'num_subpackets:{num_subpackets}')
            for sp in range(num_subpackets):
                parse_packet(packet)

parse_packet(packet)

print(f'part1: {version_sum}')