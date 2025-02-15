f = open("exons.txt")
tx_len = dict()
for line in f:
    line = line.rstrip("\n")
    cols = line.split("\t")
    tx = cols[4]
    start = int(cols[1])
    end = int(cols[2])
    ex_size = end - start
    if not tx in tx_len:
        tx_len[tx] = ex_size
    else:
        tx_len[tx] =  tx_len[tx] + ex_size
for tx in tx_len:
    if tx_len[tx] > 200:
        print(tx + "\t" + str(tx_len[tx]))