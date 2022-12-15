payload = "10FA0E00"

print(bytes.fromhex(payload))

my_hexdata = "10"
scale = 16 ## equals to hexadecimal
num_of_bits = 8
res_1 = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

# print(res_1)

my_binary = "0"
scale = 2 ## equals to binary
num_of_bits = 2
res_2 = bin(int(my_binary, scale))[2:].zfill(num_of_bits)

# print(res_2)


my_binary = "110"
scale = 2 ## equals to decimal
res_3 = int(my_binary, scale)

# print(res_3)

# bit = [0, 1, 2, 3, 4, 5, 6, 7]
# bit = '00001000'
# bit = '12345678'

# print(bit[:3])
# print(bit[3])
# print(bit[4])
# print(bit[5:])