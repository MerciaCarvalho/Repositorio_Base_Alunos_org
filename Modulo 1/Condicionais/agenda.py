import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else "clear")

def adiciona_nome(lista_nomes, nome):
    lista_nomes.append(nome) #Adiciona nome na lista nome_nome0
   
def remover_nome(lista_nomes, nome):
    if nome in lista_nomes:
        lista_nomes.remove(nome)

def mostrar_nomes(lista_nomes):
    for nome in lista_nomes: #[João]
        print(nome)

nomes = []
while True:
    limpa_tela()
    nomes = []
    menu = input("Escolha sua opção:\n[1] - Listar nomes\n[2] - Adicionar nomes\n[3] - Remover nomes\n[0] - Sair\nSua opção: ")
    if menu == "0":
        break
    elif menu == "1":
        mostrar_nomes(nomes)
        input("Aperte Enter para continuar")
    elif menu == "2":
        nome_salvar = input("Digite o nome que deseja adicionar: ")
        adiciona_nome(nomes, nome_salvar)
    elif menu == "3":
        remover_nome = input("Digite o nome que deseja remover: ")
        remover_nome(nomes, remover_nome)
    else:
        print("Opção inválida.")
        input("Aperte Enter para continuar")
