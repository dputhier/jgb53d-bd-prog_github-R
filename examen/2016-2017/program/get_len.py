fh = open("transcript.fasta")
nb = dict()
for l in fh:    
    l = l.rstrip("\n")
    if l.startswith(">"):
        l = l.lstrip(">")
        f = l.split("|")
        t = f[0]
        if t not in nb:
            nb[t] =1
        else:
            nb[t] +=1
fh.close()
fh = open("transcript.fasta")
print(nb)
for l in fh:
    l = l.rstrip("\n")
    if l.startswith(">"):
        h = l
        l = l.lstrip(">")
        f = l.split("|")
        t = f[0]        
    else:
        if nb[t] >= 4 :
            print(h)
            print(l)