import random 
import argparse 
file = open("slowa.txt", 'r', encoding = "utf-8")
lista = [] 
for word in file : 
	lista.append(word)
file.close()

random.shuffle(lista)
parser = argparse.ArgumentParser(description = "generuje losowe dane") 
parser.add_argument("size", type = int, help = "liczba dancych") 
args = parser.parse_args()

for x in range(0, args.size): 
	print(lista[x], end = "") 


