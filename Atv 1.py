estoque = []

def adicionar_produto(estoque):
    produto = input("Qual produto deseja adicionar ao estoque? ")

    if produto in estoque:
        print("O item já pertence à lista")

    else:
        estoque.append(produto)

def buscar_produto(estoque):
    produto = input("Qual o produto que será verificado? ")

    if produto in estoque:
        print("Produto disponivel")

    else:
        print("Produto esgotado")

def listar_estoque(estoque):
    print(estoque)

def menu():
    while True:
        escolha = input("\n1 - Adicionar produto\n2 - Buscar produto\n3 - Listar estoque\n4 - Sair\n\n")
        if escolha == "1":
            adicionar_produto(estoque)

        elif escolha == "2":
            buscar_produto(estoque)

        elif escolha == "3":
            listar_estoque(estoque)

        elif escolha == "4":
            print("Saiu!")
            break

menu()