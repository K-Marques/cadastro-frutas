#Módulo_de_Função

def adicionar_fruta(lista):
    """
    Adiciona uma fruta com nome e preço à lista de frutas.
    """
    nome = input("Digite o nome da fruta: ")
    try:
        preco = float(input("Digite o preço da fruta: "))
        if preco < 0:
            raise ValueError("Preço não pode ser negativo!")
    except ValueError as e:
        print(f"Erro: {e}")
        return
    lista.append({"nome": nome, "preco": preco})
    print(f"{nome} adicionada com sucesso!")

def listar_frutas(lista):
    """
    Lista todas as frutas cadastradas.
    """
    if not lista:
        print("Nenhuma fruta cadastrada.")
        return
    print("Frutas cadastradas:")
    for fruta in lista:
        print(f"- {fruta['nome']} : R${fruta['preco']:.2f}")

def total_gasto(lista):
    """
    Calcula e retorna o total gasto em todas as frutas.
    """
    return sum(f['preco'] for f in lista)

def frutas_unicas(lista):
    """
    Retorna um conjunto com os nomes das frutas únicas.
    """
    return set(f['nome'] for f in lista)

def frutas_por_preco(lista):
    """
    Retorna a fruta mais cara e a mais barata usando lambda.
    """
    if not lista:
        return None, None
    mais_cara = max(lista, key=lambda x: x['preco'])
    mais_barata = min(lista, key=lambda x: x['preco'])
    return mais_cara, mais_barata

#Programa_principal
frutas = []  # lista global

while True:
    print("\n===== Menu =====")
    print("1 - Adicionar fruta")
    print("2 - Listar frutas")
    print("3 - Total gasto")
    print("4 - Frutas únicas")
    print("5 - Fruta mais cara e mais barata")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_fruta(frutas)
    elif opcao == "2":
        listar_frutas(frutas)
    elif opcao == "3":
        print(f"Total gasto: R${total_gasto(frutas):.2f}")
    elif opcao == "4":
        unicas = frutas_unicas(frutas)
        print(f"Frutas únicas cadastradas: {', '.join(unicas)}")
    elif opcao == "5":
        cara, barata = frutas_por_preco(frutas)
        if cara and barata:
            print(f"Mais cara: {cara['nome']} - R${cara['preco']:.2f}")
            print(f"Mais barata: {barata['nome']} - R${barata['preco']:.2f}")
        else:
            print("Nenhuma fruta cadastrada.")
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

print("Programa encerrado.")
