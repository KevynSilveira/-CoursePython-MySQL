with open("seq.fasta", "r") as arquivo:
    linhas = arquivo.readlines()

multifasta = {}
seq_atual = None

for linha in linhas:
    linha = linha.strip()

    if linha.startswith(">"):
        seq_atual = linha[1:]
        multifasta[seq_atual] = ""
    elif seq_atual is not None:
        multifasta[seq_atual] += linha

print(multifasta.get("seq2", "Sequence 'seq2' not found."))
