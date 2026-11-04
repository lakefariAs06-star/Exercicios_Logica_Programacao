catalogo = [
    {"nome": "Batom Matte Vermelho", "preco": "45.90"},
    {"nome": "Hidratante Facial CeraVe", "preco": "89.90"},
    {"nome": "Perfume La Vie Est Belle", "preco": "299.00"}
]

while True:
    print("\n--- CATÁLOGO DE BELEZA ---")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_prod = input("Nome do produto de beleza: ")
        preco_prod = input("Preço (R$): ")
        catalogo.append({"nome": nome_prod, "preco": preco_prod})
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        if not catalogo:
            print("\nO catálogo está vazio.")
        else:
            print("\n--- LISTA DE PRODUTOS ---")
            for i, p in enumerate(catalogo, 1):
                print(f"{i}. {p['nome']} - R$ {p['preco']}")

    elif opcao == "3":
        print("A sair do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
