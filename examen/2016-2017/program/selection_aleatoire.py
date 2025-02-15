# -*- coding: utf-8 -*-

############################################################
# Un programme permettant de lire le fichier "transcript.fasta"
# et de sélectionner au hasard 10 transcripts
# dont les séquences des exons correspondant seront
# imprimées au format FASTA.
# last modification: 03 Fev 2017
# @author: D. Puthier
###########################################################

from random import randint

# Variable definition
NB_RANDOM = 2
transcript_list = set()
selected_transcripts = list()

# reading the file

file_handler = open("transcript.fasta", "r")

for line in file_handler:
    line = line.rstrip("\n")
    if line.startswith(">"):
        line = line.lstrip(">")
        fields = line.split("|")
        tx_name =fields[0]
        transcript_list.add(tx_name)


transcript_list = list(transcript_list)

for i in range(NB_RANDOM):
    pos = randint(0,len(transcript_list)-1)
    selected_transcripts += [transcript_list[pos]]
    transcript_list.remove(transcript_list[pos])

file_handler = open("transcript.fasta", "r")

for line in file_handler:

    line = line.rstrip("\n")
    if line.startswith(">"):
        line = line.lstrip(">")
        fields = line.split("|")
        tx_name =fields[0]
        to_print = False
        if tx_name in selected_transcripts: 
            print(line)
            to_print = True
            
    else:
        if to_print:
            print(line)
            to_print = False

