import random

# Dicionário de produtos (mini banco de dados)

produtos = {
    "Arroz": {"preço": 25.00,"estoque": 40},
    "Feijão": {"preço": 20.00,"estoque": 35},
    "Macarrão": {"preço": 10.00,"estoque": 30},
    "Óleo": {"preço": 10.00 ,"estoque": 30 },
    "Açúcar": {"preço": 15.00,"estoque": 40},
    "Café": {"preço": 14.00,"estoque": 30},
}

# Variável que armazena o total de vendas feitas

total_vendas = 0.0

# Função para cadastrar produtos novos

def cadastrar_produtos():
    nome = input("Digite o nome do produto: ")
    preco = float("Digite o preço selecionado para {nome}: ")
    estoque = int("Dê a quantidade no estoque de {nome}: ")
    produtos[nome] = {"preço": preco, "estoque": estoque}
    print(f"Produto cadastrado no sistema com êxito!\n")

# Função para solicitar a lista de produtos disponíveis a venda

def exibir_produtos():
    print(f"\n Produtos disponíveis:")
    for produto, info in produtos.items():
        print(f"{produto} - Preço: {info["preço"]:.2f}, Estoque: {info["estoque"]} unidades")
    print()

# Função para fazer uma compra de algum produto

def realizar_vendas():
    global total_vendas
    produto_vendido = input("Digite o nome do produto que deseja comprar: ")

# Função para verficar a existência do produto no estoque

    if produto_vendido in produtos:
        quantidade = int(input("Digite quantas unidades de {produto_vendido} deseja comprar:"))
        if produtos[produto_vendido]["estoque"] >= quantidade:
          valor_venda = quantidade * produtos[produto_vendido]["preço"]
          produtos[produto_vendido]["estoque"] -= quantidade
          total_vendas += valor_venda
          print(f"Venda realizada: {quantidade}x {produto_vendido - Total: R${valor_venda:.2f}}\n")

        else:
          print(f"Quantidade de produtos insuficiente.\n")

    else:
       print(f"Produto não encontrado.")

    # Função 
