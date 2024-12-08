from datetime import datetime

# Classes Cliente, Produto, Vendedor e Venda permanecem as mesmas

class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}")


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_dados(self):
        print(f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}")


class Vendedor:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def exibir_dados(self):
        print(f"Vendedor: {self.nome}, Matrícula: {self.matricula}, Email: {self.email}")


class Venda:
    def __init__(self, cliente, produto, vendedor, quantidade, data_venda):
        self.cliente = cliente
        self.produto = produto
        self.vendedor = vendedor
        self.quantidade = quantidade
        self.data_venda = data_venda

    def exibir_dados(self):
        valor_total = self.produto.preco * self.quantidade
        print(f"Cliente: {self.cliente.nome}, Produto: {self.produto.nome}, "
              f"Quantidade: {self.quantidade}, Total: R$ {valor_total:.2f}, "
              f"Vendedor: {self.vendedor.nome}, Data: {self.data_venda}")


class Gerenciador:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.vendedores = []
        self.vendas = []

    # Métodos para buscar itens por índice
    def buscar_por_indice(self, lista, tipo):
        if not lista:
            print(f"Nenhum {tipo} cadastrado.")
            return None

        print(f"\nSelecione um {tipo}:")
        for i, item in enumerate(lista):
            print(f"{i + 1}. {item.nome if hasattr(item, 'nome') else 'Venda'}")
        indice = int(input(f"Escolha o número do {tipo}: ")) - 1

        if 0 <= indice < len(lista):
            return lista[indice]
        else:
            print("Opção inválida.")
            return None

    # Métodos para gerenciar clientes
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        print("\nLista de Clientes:")
        for cliente in self.clientes:
            cliente.exibir_dados()

    def editar_cliente(self):
        cliente = self.buscar_por_indice(self.clientes, "cliente")
        if cliente:
            cliente.nome = input("Digite o novo nome do cliente: ")
            cliente.idade = int(input("Digite a nova idade do cliente: "))
            cliente.email = input("Digite o novo email do cliente: ")
            print("Cliente atualizado com sucesso!")

    def excluir_cliente(self):
        cliente = self.buscar_por_indice(self.clientes, "cliente")
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente removido com sucesso!")

    # Métodos para gerenciar produtos
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado com sucesso!")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("\nLista de Produtos:")
        for produto in self.produtos:
            produto.exibir_dados()

    def editar_produto(self):
        produto = self.buscar_por_indice(self.produtos, "produto")
        if produto:
            produto.nome = input("Digite o novo nome do produto: ")
            produto.preco = float(input("Digite o novo preço do produto: "))
            print("Produto atualizado com sucesso!")

    def excluir_produto(self):
        produto = self.buscar_por_indice(self.produtos, "produto")
        if produto:
            self.produtos.remove(produto)
            print("Produto removido com sucesso!")

    # Métodos para gerenciar vendedores
    def adicionar_vendedor(self, vendedor):
        self.vendedores.append(vendedor)
        print(f"Vendedor {vendedor.nome} adicionado com sucesso!")

    def listar_vendedores(self):
        if not self.vendedores:
            print("Nenhum vendedor cadastrado.")
            return
        print("\nLista de Vendedores:")
        for vendedor in self.vendedores:
            vendedor.exibir_dados()

    def editar_vendedor(self):
        vendedor = self.buscar_por_indice(self.vendedores, "vendedor")
        if vendedor:
            vendedor.nome = input("Digite o novo nome do vendedor: ")
            vendedor.matricula = input("Digite a nova matrícula do vendedor: ")
            vendedor.email = input("Digite o novo email do vendedor: ")
            print("Vendedor atualizado com sucesso!")

    def excluir_vendedor(self):
        vendedor = self.buscar_por_indice(self.vendedores, "vendedor")
        if vendedor:
            self.vendedores.remove(vendedor)
            print("Vendedor removido com sucesso!")

    # Métodos para gerenciar vendas
    def registrar_venda(self):
        if not self.clientes or not self.produtos or not self.vendedores:
            print("Certifique-se de que há clientes, produtos e vendedores cadastrados antes de registrar uma venda.")
            return

        cliente = self.buscar_por_indice(self.clientes, "cliente")
        produto = self.buscar_por_indice(self.produtos, "produto")
        vendedor = self.buscar_por_indice(self.vendedores, "vendedor")
        quantidade = int(input("Digite a quantidade do produto: "))
        data_venda = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if cliente and produto and vendedor:
            nova_venda = Venda(cliente, produto, vendedor, quantidade, data_venda)
            self.vendas.append(nova_venda)
            print(f"Venda registrada com sucesso!")

    def listar_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada.")
            return
        print("\nLista de Vendas:")
        for venda in self.vendas:
            venda.exibir_dados()

    def excluir_venda(self):
        venda = self.buscar_por_indice(self.vendas, "venda")
        if venda:
            self.vendas.remove(venda)
            print("Venda removida com sucesso!")

    def consultar_lucro_do_mes(self, mes, ano):
        lucro = 0
        for venda in self.vendas:
            data_venda = datetime.strptime(venda.data_venda, "%d/%m/%Y %H:%M:%S")
            if data_venda.month == mes and data_venda.year == ano:
                lucro += venda.produto.preco * venda.quantidade
        print(f"Lucro total em {mes:02d}/{ano}: R$ {lucro:.2f}")


def main():
    gerenciador = Gerenciador()

    while True:
        print("\n==== Gerenciador ====")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Editar Cliente")
        print("4. Excluir Cliente")
        print("5. Adicionar Produto")
        print("6. Listar Produtos")
        print("7. Editar Produto")
        print("8. Excluir Produto")
        print("9. Adicionar Vendedor")
        print("10. Listar Vendedores")
        print("11. Editar Vendedor")
        print("12. Excluir Vendedor")
        print("13. Registrar Venda")
        print("14. Listar Vendas")
        print("15. Excluir Venda")
        print("16. Consultar Lucro do Mês")
        print("17. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            email = input("Digite o email do cliente: ")
            gerenciador.adicionar_cliente(Cliente(nome, idade, email))
        elif opcao == "2":
            gerenciador.listar_clientes()
        elif opcao == "3":
            gerenciador.editar_cliente()
        elif opcao == "4":
            gerenciador.excluir_cliente()
        elif opcao == "5":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            gerenciador.adicionar_produto(Produto(nome, preco))
        elif opcao == "6":
            gerenciador.listar_produtos()
        elif opcao == "7":
            gerenciador.editar_produto()
        elif opcao == "8":
            gerenciador.excluir_produto()
        elif opcao == "9":
            nome = input("Digite o nome do vendedor: ")
            matricula = input("Digite a matrícula do vendedor: ")
            email = input("Digite o email do vendedor: ")
            gerenciador.adicionar_vendedor(Vendedor(nome, matricula, email))
        elif opcao == "10":
            gerenciador.listar_vendedores()
        elif opcao == "11":
            gerenciador.editar_vendedor()
        elif opcao == "12":
            gerenciador.excluir_vendedor()
        elif opcao == "13":
            gerenciador.registrar_venda()
        elif opcao == "14":
            gerenciador.listar_vendas()
        elif opcao == "15":
            gerenciador.excluir_venda()
        elif opcao == "16":
            mes = int(input("Digite o mês (1-12): "))
            ano = int(input("Digite o ano: "))
            gerenciador.consultar_lucro_do_mes(mes, ano)
        elif opcao == "17":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
