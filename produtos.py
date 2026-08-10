Produtos = []

def cadastrarProduto():
    print("\n===== Cadastrando produto: =====")
    
    try:
        nome = input("Insira o nome do produto: ")
        preco = float(input("Insira o valor do produto: R$"))
    except:
        print("Valor inválido. Tente novamente.")
        return

    Produtos.append(Produto(nome, preco))
    print(f"Produto {nome} cadastrado com valor de R${preco}.")

def listarProdutos():
    print("===== Produtos cadastrados: =====")

    for index in range(len(Produtos)):
        produto = Produtos[index]

        print(f"[{index}]")
        produto.exibir()

def comprarProduto():
    print("===== Comprando produto: =====")

    try:
        produto = Produtos[int(input("Insira o índice do produto: "))]
        qtd = int(input("\nInsira a quantidade de produtos a comprar: "))
    except:
        print("Produto ou quantidade inválida. Tente novamente.")
        return

    produto.exibir()
    total = produto.Preco * qtd

    print(f"\nO total a ser pago é de: R${total}")

    if total >= 100:
        print("Há um desconto disponível para esta compra!\n")


class Produto:
    def __init__(self, nome, preco):
        self.Nome = nome
        self.Preco = preco

    def exibir(self):
        print(f"Produto: {self.Nome} \nPreço unitário: {self.Preco}")

while True:
    print("\n===== Escolha uma ação: =====\n[1] Cadastrar produto \n[2] Ver produtos \n[3] Comprar produto \n[4] Encerrar programa \n")
    
    try:
        escolha = int(input())
    except:
        print("Valor inválido. Tente novamente.")
        continue

    if escolha == 1:
        cadastrarProduto()

    elif escolha == 2:
        listarProdutos()

    elif escolha == 3:
        comprarProduto()

    elif escolha == 4:
        print("===== ENCERRANDO PROGRAMA =====")
        break

    else:
        print("Opção inexistente. Tente novamente.")
