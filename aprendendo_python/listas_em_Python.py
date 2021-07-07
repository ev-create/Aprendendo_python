# Listas

vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')

# Mesmo resultado

vogais = []

print(f"\nTipo de objetos vogais = {type(vogais)}\n")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}\n")

frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print(f"maça" in frutas) # True
print(f"abacate" in frutas) # False
print(f"abacate" not in frutas) # True
print(min(frutas)) # banana
print(max(notas)) # 10
print(frutas.count("maça")) # 2
print(frutas + notas)
print(2 * frutas)

lista = ['Python', 30.61, "Java", 51, ['a', 'b', 20], "maça"]

print(f"\nTamanho da lista = {len(lista)}\n")
for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} --------------> tipo individual = {type(item)}")

print(f"\nExemplos de slices:\n")

print("lista[1] = ", lista[1])
print("lista[0:2] = ", lista[0:2])
print("lista[:2] = ", lista[:2])
print("lista[3:5] = ", lista[3:5])
print("lista[3:6] = ", lista[3:6])
print("lista[3:] = ", lista[3:])
print("lista[-2] = ", lista[-2])
print("lista[-1] = ", lista[-1])
print("lista[4][1] = ", lista[4][1])

linguagens = ["Python", "Java", "JavaScript", "C", 'C#', 'C++', "Swift", "Go", "Kotlin" ]
# linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa Sintaxe produz o mesmo resultado que a linha 1.

print(f"\nantes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]

print(f"\nDepois da listcomp = ", linguagens)

# Metodo usando sintaxe .split()

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print(f"\nAntes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print(f"\nDepois da listcomp = ", linguagens)

# listcomp somente com a frase java no texto

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = [item for item in linguagens if "Java" in item]

print(linguagens_java)

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = []
for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)

print(linguagens_java)

# FUNÇÕES map() e filter()

# Exemplo 1

print(f"\nExemplo 1")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"nova lista é = , {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

# Exemplo 2

print(f"\n\nExemplo 2")
numeros = [0, 1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x * x, numeros))
print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")

numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Tupla

print(numeros_pares)

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"\nTipo de objetos vogais = {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

#vogais = ()
#vogais.append('a')

vogais = ['a', 'e', 'i', 'o', 'u']
for item in enumerate(vogais):
    print(item)

# print(tuple(enumerate(vogais)))
# print(list(enurmerate(vogais)))










