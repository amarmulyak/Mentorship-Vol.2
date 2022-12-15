payload = "10FA0E00"


def convert_hex_bytes_to_bit(hex_data: str):
    scale = 16
    num_of_bits = 8

    return bin(int(hex_data, scale))[2:].zfill(num_of_bits)


def convert_bit_to_int(bit_data: str):
    scale = 2
    return int(bit_data, scale)


def convert_byte_1_to_bits(byte: str):
    bit = convert_hex_bytes_to_bit(byte)

    field_1 = bit[:3]
    field_2 = bit[3]
    field_3 = bit[4]
    field_4 = bit[5:]

    return field_1, field_2, field_3, field_4

def get_field_1(field_1: str):
    field1_data = {
        '0': 'Low',
        '1': 'reserved',
        '2': 'reserved',
        '3': 'reserved',
        '4': 'Medium',
        '5': 'reserved',
        '6': 'reserved',
        '7': 'High'
    }

    return field1_data[convert_bit_to_int(field_1)]


def get_field_4(field_4: str):
    field4_data = {
        '0': '00',
        '1': '10',
        '2': '20',
        '3': '30',
        '4': '40',
        '5': '50',
        '6': '60',
        '7': '70'
    }

    return field4_data[convert_bit_to_int(field_4)]

def convert_payload_to_bytes(payload: str):
    byte_1 = payload[:2]
    byte_2 = payload[2:4]
    byte_3 = payload[4:6]
    byte_4 = payload[6:]

    return byte_1, byte_2, byte_3, byte_4
