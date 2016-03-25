import string

# Download from http://www.gutenberg.org/cache/epub/11/pg11.txt
dicipalavra = {}
arqui = open("C:\Users\Eduardo\Downloads\pg11.txt")
# Eduardo teste1.
for sss in arqui:
    sss = sss.lower()
    sss = sss.translate(None, string.punctuation)
    palavras = sss.split()
    for palavra in palavras:

        if palavra not in dicipalavra:
            dicipalavra[palavra] = 0
        else:
            dicipalavra[palavra] += 1
lista = []
for contagem in dicipalavra.keys():
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
