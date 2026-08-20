class Produto:
    def __init__(self, codigo, nome, quant, preco):
        self.Codigo = codigo
        self.Nome = nome
        self.Quant = quant
        self.Preco = preco

    def mostrar(self):
        print("Código do Produto: ", self.Codigo)
        print("Nome do Produto: ", self.Nome)
        print("Quantidade de Produto: ", self.Quant)
        print("Preço do produto: ", self.Preco)

Nescau = Produto(22, "Nescau", 2, 11)
Nescau.mostrar()
