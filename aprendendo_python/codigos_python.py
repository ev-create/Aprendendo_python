cadastro = {
        'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
        'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
        'idade' : [25, 33, 37, 18]

}
print("len(cadastro = ", len(cadastro))

print("\n cadastro.keys() =\n", cadastro.keys())
print("\n cadastro.values() = \n", cadastro.keys())
print("\n cadastro.items = \n", cadastro.items())

print("\n cadastro['nome'] = \n", cadastro['nome'])
print("\n cadastro['nome'][2] = \n", cadastro['nome'][2])
print("\n cadastro['idade][2:] = \n", cadastro['idade'][2:])

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

qtde_item = sum([len(cadastro[chave]) for chave in cadastro])

print(f"Quantidade de elementos no dicionário = {qtde_item}")