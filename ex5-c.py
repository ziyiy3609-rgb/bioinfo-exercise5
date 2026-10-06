from Bio import SeqIO
import os

try:
    name = input("Enter file name: ")
    input_handle = open(name, "r")
except:
    print("File " + str(name) + " not found! Check file name and extension.")
    quit()

output = os.path.splitext(name)[0]+".fasta"
output_handle = open(output, "w")
sequences = SeqIO.parse(input_handle, "fasta")
count = SeqIO.write(sequences, output_handle, "fasta")
print(f"Wrote {count} records to {output}")
input_handle.close()
output_handle.close()
