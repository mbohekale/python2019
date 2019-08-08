import struct 
values = (1, bytes('ab','utf-8'), 2.7)
packer = struct.Struct('I 2s f')		#Int, char[2], float
packed_data = packer.pack(*values)
print(packed_data)


unpacker = struct.Struct('I 2s f')
unpacked_data = unpacker.unpack(packed_data)
print(unpacked_data)
