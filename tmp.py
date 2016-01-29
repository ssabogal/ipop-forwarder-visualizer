

nr_nodes=20

ip4_addr="192.168.0.10"
ip4_mask=16


parts = ip4_addr.split('.')
tmp = (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

for i in range(nr_nodes):
    p0 = ((tmp + i) >> 24) & 0xFF
    p1 = ((tmp + i) >> 16) & 0xFF
    p2 = ((tmp + i) >>  8) & 0xFF
    p3 = ((tmp + i) >>  0) & 0xFF

    ip4 = str(p0) + "." + str(p1) + "." + str(p2) + "." + str(p3)

    print(ip4)
