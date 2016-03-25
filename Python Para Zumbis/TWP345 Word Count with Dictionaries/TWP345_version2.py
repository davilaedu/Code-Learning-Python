import string

# Download from http://www.gutenberg.org/cache/epub/11/pg11.txt
dicipalavra = {}
arqui = open("C:\Users\Eduardo\Downloads\pg11.txt")
# Eduardo Teste2.
for line in arqui:
    line = line.lower()
    line = line.translate(None, string.punctuation)
    words = line.split()
    for word in words:
        dicipalavra[word] = dicipalavra.get(word, 0) + 1
lista = []
for contagem in dicipalavra.keys():
    # wnovox
    lista.append((dicipalavra[contagem], contagem))
lista.sort(reverse=True)
print lista
arqui.close()
"""
# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

for key, val in lst[:10] :
    print key, val


"""
