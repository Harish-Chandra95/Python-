import csv
import re
from collections import Counter

codon_dict = {}
# reading from tsv file
with open("D:\Downloads\\codon.tsv") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for cols in reader:
    #creating dictionary
    codon_dict[cols[0]] = cols[1]
  #entering input
  dna_seq = input(" enter the input sequence: ")
  # forming indivudual sequence using regular expression
  codons=(re.findall(r'.{1,3}',dna_seq))
  print("the individual codon sequence are: ", codons)
  # returns name of condons
  codon_names = list(map(lambda x: codon_dict[x], codons))
# count of codons
dna_counts = (codon_names)
print("the names and count of codons: ", Counter(dna_counts))