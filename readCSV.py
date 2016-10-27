import csv
import json

def readFile(fich):

    with open(fich) as dados:
        leitor = csv.DictReader(filter(lambda linha: linha[0] != "#", dados)) # ignora todas as linhas que comecem com '#'
        out = json.dumps( [ linha for linha in leitor ] )

    return out


#readFile("avioes2.csv")


