import pytest

payload = "10FA0E00"

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

field8_data = {
    '0': 'Very Low',
    '1': 'reserved',
    '2': 'Low',
    '3': 'reserved',
    '4': 'Medium',
    '5': 'High',
    '6': 'reserved',
    '7': 'Very High',
}

def convert_hex_to_bits(hex_data: str, reverse: bool = True):
    scale = 16
    num_of_bits = 8
    bits = bin(int(hex_data, scale))[2:].zfill(num_of_bits)

    if reverse:
        return bits[::-1]

    return bits


def convert_bit_to_int(bit_data: str):
    scale = 2

    return int(bit_data, scale)


def get_data_from_payload(payload: str):

    def get_bytes_from_payload(payload: str):
        byte_1 = payload[:2]
        byte_2 = payload[2:4]
        byte_3 = payload[4:6]
        byte_4 = payload[6:]

        return byte_1, byte_2, byte_3, byte_4

    def parse_byte_1(byte_1: str):
        bits = convert_hex_to_bits(byte_1)
        field_1_key = str(convert_bit_to_int(bits[:3]))
        field_4_key = str(convert_bit_to_int(bits[5:]))

        field_1 = field1_data[field_1_key]
        field_2 = bits[3].zfill(2)
        field_3 = bits[4].zfill(2)
        field_4 = field4_data[field_4_key]

        return field_1, field_2, field_3, field_4

    def parse_byte_2(byte_2: str):
        bits = convert_hex_to_bits(byte_2)
        field_8_key = str(convert_bit_to_int(bits[3:6]))

        field_5 = bits[0].zfill(2)
        field_6 = bits[1].zfill(2)
        field_7 = bits[2].zfill(2)
        field_8 = field8_data[field_8_key]

        return field_5, field_6, field_7, field_8

    def parse_byte_3(byte_3: str):
        bits = convert_hex_to_bits(byte_3)

        field_9 = bits[0].zfill(2)
        field_10 = bits[5].zfill(2)

        return field_9, field_10

    byte_1, byte_2, byte_3, byte_4 = get_bytes_from_payload(payload)
    field_1, field_2, field_3, field_4 = parse_byte_1(byte_1)
    field_5, field_6, field_7, field_8 = parse_byte_2(byte_2)
    field_9, field_10 = parse_byte_3(byte_3)

    parsed_data = {
        'field1': field_1,
        'field2': field_2,
        'field3': field_3,
        'field4': field_4,
        'field5': field_5,
        'field6': field_6,
        'field7': field_7,
        'field8': field_8,
        'field9': field_9,
        'field10': field_10
    }

    return parsed_data

payload_1 = '10FA0E00'
expected_payload_1_parsed = {'field1': 'Low',
                             'field2': '00',
                             'field3': '01',
                             'field4': '00',
                             'field5': '00',
                             'field6': '01',
                             'field7': '00',
                             'field8': 'Very High',
                             'field9': '00',
                             'field10': '00'}


@pytest.mark.parametrize('payload, expected_parsed_payload',
                         [(payload_1, expected_payload_1_parsed)])
def test_payload(payload, expected_parsed_payload):
    actual_parsed_payload = get_data_from_payload(payload)

    assert actual_parsed_payload == expected_payload_1_parsed
