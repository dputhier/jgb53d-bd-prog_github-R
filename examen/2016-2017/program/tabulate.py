file_handler = open("transcript.fasta")
n=0
for line in file_handler:    
    if n == 0:
        print("transcript\texon_number\tstrand\tsequence")
    line = line.rstrip("\n")
    if line.startswith(">"):
        line = line.lstrip(">")
        fields = line.split("|")
        transcript = fields[0]
        strand = fields[2]
        exon_number = fields[1]
        header =  transcript + "\t" +  exon_number + "\t" + strand
    else:
        print(header + "\t" + line)
    n += 1