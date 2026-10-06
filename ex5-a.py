from random import choice

def generate_random_seq(length):
    bases = ['A', 'C', 'G', 'T']
    length = int(length)
    sequence = [choice(bases) for i in range(length)]
    sequence = ''.join(sequence)
    return sequence

seq_len = input("Enter the length of sequence that you want to generate: ")
out_seq = generate_random_seq(seq_len)
print(out_seq)
