 # Categorias Registradas

Categorias = ["Eletronicos", "Som", "Celular", "Livros"]

#Variaveis de compras

CumpomDesconto = False

ValorCompra = 0.0

Carrinho = []

#Produtos cadastrados

    # Dicionario "marca","Preço","Categoria"

Produtos = {"Computador":["Acer AMD",2.050,"Eletronicos"], 
            'JBL':["JBL", 1.000, "Som"], 
            "Note":["Note 20", 3.120, 'Celular'],
            'Livro':['Pequeno Principe', 54.60, 'Livros']}


def CalculoDeImpostos(Categoria):

    """

        Calculadora de impostos para cada categoria:

            Categoria: Parametro para saber como será calculado o imposto

    """

    if Categoria == "Eletronicos":

        print("Imposto Aplicados!")

        return 450*2
    
    if Categoria == "Som":

        print("Imposto Aplicados!")

        return 250*2
    
    if Categoria == "Celular":

        print("Imposto Aplicado!")

        return 650*2

    if Categoria == "Livros":

        print("Imposto Aplicado!")

        return 50*2

def DescontosProdutos(Categoria,Quantidade):

    """

        Caculo de cada Desconto por categoria e por quantidade

            Categoria: Qual Categoria vai ser analisada

            Quantidade: Quantos itens o cliente esta comprando

    """

    if Categoria == "Eletronicos" and Quantidade >=2:

        return 200.20

    if Categoria == "Som" and Quantidade >=3:

        return 250.20

    if Categoria == "Celular" and Quantidade >=4:

        return 450.20

    if Categoria == "Livros" and Quantidade >=10:

        return 180.20

def AdicionarCarrinho(Item,Quantidade):

    """

        Função que armazena a compra do usuario:

            Item: qual Item deseja aplicar ao carrinho

            Quantidade: Quantidade Comprada daquele item

    """

    return Carrinho.append(f"{Item} {str(Quantidade)}")
   
def SistemaCalculoFinanceiro():

    # Crie o seu codigo Aqui!!

    print("SISTEMA DE COMPRAS PARA E-Comerce!")
    escolher_produto = input("Qual produto deseja:    ")
    quantidade_escolhida = input("Qual a quantidade:   ")
    print(Produtos[escolher_produto][1])
    ValorCompra = Produtos[escolher_produto][1]*int(quantidade_escolhida)
    print(ValorCompra)
    ValorCompra = ValorCompra - DescontosProdutos(Produtos[escolher_produto][2], int(quantidade_escolhida))
    ValorCompra = ValorCompra + CalculoDeImpostos(Produtos[escolher_produto][2])

    print(f"A compra resultou em R$ {ValorCompra} deseja continuar? ")
    if input("Digite s para continuar:  ") == "s":
        AdicionarCarrinho(Produtos[escolher_produto][2], int[quantidade_escolhida])
    else:
        print("Compra Cancelada!!")    
    return ValorCompra
    
while True:

    if SistemaCalculoFinanceiro() == 0.0:

        print("O usuario não comprou nenum item 😢")

    else:

        print(f"Carrinho do usuario 🛒")

        for i in Carrinho:

            print(i)