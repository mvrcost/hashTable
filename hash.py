def valorHash(student):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    valor = 0
    for l in student:
        if l.upper() in alfabeto:  
            valor += alfabeto.index(l.upper()) + 1
    return valor % 10



def insert_hashing(tabelaHash, student):
    codHash = valorHash(student)
    tabelaHash[codHash].append(student)


def print_tabela(tabelaHash):
    for index, nomes in enumerate(tabelaHash):
        if nomes:
            print(f"{index}: {' '.join(nomes)}")


N = int(input())
tabelaHash = [[] for _ in range(10)]

for i in range(N):
    estudante = input()
    insert_hashing(tabelaHash, estudante)


print_tabela(tabelaHash)
